from django.contrib.messages import get_messages
from django.urls import reverse
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


class CheckUserAuthenticatedMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            messages.add_message(request, messages.INFO, '请先登录')
            return redirect(to=reverse("login"))
        else:
            return super(CheckUserAuthenticatedMixin, self).dispatch(request, *args, **kwargs)


class Base(View):
    def get(self, request, *args, **kwargs):
        return render(request=request, template_name="base.html")


class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request=request, template_name="index.html", context={"messages": get_messages(request)})


class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request=request, template_name="login.html", context={"messages": get_messages(request)})

    def post(self, request, *args, **kwargs):
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            messages.add_message(request, messages.INFO, '登录成功')
            return redirect(to=reverse("index"))
        else:
            messages.add_message(request, messages.INFO, '登录失败')
            return redirect(to=reverse("index"))


class Logout(CheckUserAuthenticatedMixin, View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(request, messages.INFO, '成功退出系统， 您当前已退出。')
        return redirect(to="login")
