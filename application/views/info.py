from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.contrib.messages import get_messages
from application.models import Institute, Admin, Major, Class
from application.views import CheckUserAuthenticatedMixin


class InstituteInfoView(CheckUserAuthenticatedMixin, View):
    def get(self, request, *args, **kwargs):
        get_params = request.GET.dict()
        institute_id = get_params.get("institute_id", None)
        detail_institute = None
        admins = None
        if institute_id:
            detail_institute = Institute.objects.filter(id=institute_id).first()
            admins = Admin.objects.all()
            if detail_institute is None:
                return redirect(to="institute_info")
        institutes = Institute.objects.all()

        return render(request=request,
                      template_name="info/institute.html",
                      context={
                          'institutes': institutes,
                          'detail_institute': detail_institute,
                          'admins': admins,
                          'messages': get_messages(request)
                      })

    def post(self, request, *args, **kwargs):
        institute_name = request.POST['institute_name']
        institute_id = request.POST['hidden_id']
        admin_id = request.POST['user_id']
        institute_obj = Institute.objects.get(id=institute_id)
        admin_obj = Admin.objects.get(id=admin_id)
        institute_obj.name = institute_name
        institute_obj.create_by = admin_obj
        institute_obj.save()
        messages.add_message(request, messages.INFO, '修改学院信息成功')
        return redirect(to='institute_info')


class MajorInfoView(CheckUserAuthenticatedMixin, View):
    def get(self, request, *args, **kwargs):
        majors = Major.objects.all()
        institutes = Institute.objects.all()
        admins = None
        detail_major = None
        get_params = request.GET.dict()
        major_id = get_params.get("major_id", None)
        if major_id:
            detail_major = Major.objects.filter(id=major_id).first()
            admins = Admin.objects.all()
            if detail_major is None:
                return redirect(to="major_info")

        return render(request=request,
                      template_name="info/major.html",
                      context={
                          "majors": majors,
                          'admins': admins,
                          'detail_major': detail_major,
                          'institutes': institutes,
                          'messages': get_messages(request)
                      })

    def post(self, request, *args, **kwargs):
        major_name = request.POST['major_name']
        major_id = request.POST['hidden_id']
        institute_id = request.POST['institute_id']
        admin_id = request.POST['admin_id']

        major_obj = Major.objects.get(id=major_id)
        institute_obj = Institute.objects.get(id=institute_id)
        admin_obj = Admin.objects.get(id=admin_id)

        major_obj.name = major_name
        major_obj.create_by = admin_obj
        major_obj.institute = institute_obj
        major_obj.save()
        messages.add_message(request, messages.INFO, '修改专业信息成功')
        return redirect(to='major_info')


class ClassInfoView(CheckUserAuthenticatedMixin, View):
    def get(self, request, *args, **kwargs):
        majors = Major.objects.all()
        classes = Class.objects.all()
        admins = None
        detail_class = None
        get_params = request.GET.dict()
        class_id = get_params.get("class_id", None)
        if class_id:
            detail_class = Class.objects.filter(id=class_id).first()
            admins = Admin.objects.all()
            if detail_class is None:
                return redirect(to="class_info")

        return render(request=request,
                      template_name="info/class.html",
                      context={
                          "classes": classes,
                          'admins': admins,
                          'detail_class': detail_class,
                          'majors': majors,
                          'messages': get_messages(request)
                      })

    def post(self, request, *args, **kwargs):
        class_name = request.POST['class_name']
        class_id = request.POST['hidden_id']
        major_id = request.POST['major_id']
        admin_id = request.POST['admin_id']

        major_obj = Major.objects.get(id=major_id)
        class_obj = Institute.objects.get(id=class_id)
        admin_obj = Admin.objects.get(id=admin_id)

        class_obj.name = class_name
        class_obj.create_by = admin_obj
        class_obj.major = major_obj
        class_obj.save()
        messages.add_message(request, messages.INFO, '修改专业信息成功')
        return redirect(to='class_info')


class StudentInfoView(CheckUserAuthenticatedMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request=request, template_name="info/institute.html")

    def post(self, request, *args, **kwargs):
        return render(request=request, template_name="info/institute.html")


class TeacherInfoView(CheckUserAuthenticatedMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request=request, template_name="info/institute.html")

    def post(self, request, *args, **kwargs):
        return render(request=request, template_name="info/institute.html")
