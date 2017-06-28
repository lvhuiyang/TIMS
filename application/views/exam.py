from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.messages import get_messages
from application.models import Admin, Student, Exam, Course
from application.views import CheckUserAuthenticatedMixin


class ExamView(CheckUserAuthenticatedMixin, View):
    def get(self, request, *args, **kwargs):
        get_params = request.GET.dict()
        exam_id = get_params.get("exam_id", None)
        detail_exam = None
        admins = None
        courses = None
        if exam_id:
            detail_exam = Exam.objects.filter(id=exam_id).first()
            admins = Admin.objects.all()
            courses = Course.objects.all()
            if detail_exam is None:
                return redirect(to="institute_info")
        exams = Exam.objects.all()
        students = Student.objects.all()

        return render(request=request,
                      template_name="exam/exam.html",
                      context={
                          'exams': exams,
                          'courses': courses,
                          'detail_exam': detail_exam,
                          'students': students,
                          'admins': admins,
                          'messages': get_messages(request)
                      })

    def post(self, request, *args, **kwargs):
        exam_title = request.POST['exam_title']
        exam_id = request.POST['exam_id']
        admin_id = request.POST['admin_id']
        student_id = request.POST['student_id']
        course_id = request.POST['course_id']

        exam_obj = Exam.objects.get(id=exam_id)
        admin_obj = Admin.objects.get(id=admin_id)
        course_obj = Course.objects.get(id=course_id)
        student_obj = Student.objects.get(id=student_id)

        exam_obj.title = exam_title
        exam_obj.create_by = admin_obj
        exam_obj.course = course_obj
        exam_obj.student = student_obj
        exam_obj.save()
        messages.add_message(request, messages.INFO, '修改考试信息成功')
        return redirect(to='exam')


class ExamPointView(CheckUserAuthenticatedMixin, View):
    def get(self, request, *args, **kwargs):
        get_params = request.GET.dict()
        exam_id = get_params.get("exam_id", None)
        detail_exam = None
        admins = None
        courses = None
        if exam_id:
            detail_exam = Exam.objects.filter(id=exam_id).first()
            admins = Admin.objects.all()
            courses = Course.objects.all()
            if detail_exam is None:
                return redirect(to="institute_info")
        exams = Exam.objects.all()
        students = Student.objects.all()

        return render(request=request,
                      template_name="exam/score.html",
                      context={
                          'exams': exams,
                          'courses': courses,
                          'detail_exam': detail_exam,
                          'students': students,
                          'admins': admins,
                          'messages': get_messages(request)
                      })

    def post(self, request, *args, **kwargs):
        exam_title = request.POST['exam_title']
        exam_id = request.POST['exam_id']
        admin_id = request.POST['admin_id']
        student_id = request.POST['student_id']
        exam_score = request.POST['exam_score']
        try:
            score = int(exam_score)
        except Exception:
            messages.add_message(request, messages.INFO, '分数填写格式不正确')
            return redirect(to='exam_point')
        else:
            if score > 100 or score < 0:
                messages.add_message(request, messages.INFO, '请填写的整形数字在 0-100 之间')
                return redirect(to='exam_point')

        exam_obj = Exam.objects.get(id=exam_id)
        admin_obj = Admin.objects.get(id=admin_id)
        student_obj = Student.objects.get(id=student_id)

        exam_obj.title = exam_title
        exam_obj.create_by = admin_obj
        exam_obj.student = student_obj
        exam_obj.score = score
        exam_obj.save()
        messages.add_message(request, messages.INFO, '修改成绩信息成功')
        return redirect(to='exam_point')
