from django.views import View
from django.views.generic import TemplateView
from django.shortcuts import render


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request=request, template_name="index.html", context={'hello': 'world'})


class Hello(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request=request, template_name="base.html", context={'hello': 'world'})


class Login(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request=request, template_name="login.html", context={'hello': 'world'})
