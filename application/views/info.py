from django.shortcuts import render, redirect
from django.views import View

from application.models import Institute, Admin
from application.views import CheckUserAuthenticatedMixin


class InstituteInfoView(CheckUserAuthenticatedMixin, View):
    def get(self, request, *args, **kwargs):
        get_params = request.GET.dict()
        institute_id = get_params.get("institute_id", None)
        detail_institute = None
        admins = None
        if institute_id:
            detail_institute = Institute.objects.filter(id=institute_id).first()
            if detail_institute is None:
                return redirect(to="institute_info")
            admins = Admin.objects.all()
        institutes = Institute.objects.all()

        return render(request=request,
                      template_name="info/institute.html",
                      context={
                          'institutes': institutes,
                          'detail_institute': detail_institute,
                          'admins': admins
                      })

    def post(self, request, *args, **kwargs):

        return render(request=request, template_name="base.html")


class MajorInfoView(CheckUserAuthenticatedMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request=request, template_name="info/institute.html")

    def post(self, request, *args, **kwargs):
        return render(request=request, template_name="info/institute.html")


class ClassInfoView(CheckUserAuthenticatedMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request=request, template_name="info/institute.html")

    def post(self, request, *args, **kwargs):
        return render(request=request, template_name="info/institute.html")


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
