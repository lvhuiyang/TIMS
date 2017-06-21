from django.views import View
from django.shortcuts import render


class CheckUserAuthenticatedMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return render(request=request, template_name="login.html", context={"check_authenticated": True})
        else:
            return super(CheckUserAuthenticatedMixin, self).dispatch(request, *args, **kwargs)


class Base(CheckUserAuthenticatedMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request=request, template_name="base.html")


class Index(CheckUserAuthenticatedMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request=request, template_name="index.html", context={'hello': 'world'})


class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request=request, template_name="login.html", context={"check_authenticated": False})

    def post(self, request, *args, **kwargs):
        return render(request=request, template_name="my_info.html", context={})
