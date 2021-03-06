from django.contrib.messages import get_messages
from django.urls import reverse
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from application.const import ROLE_INFO
from application.models import Student, Teacher, Admin


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
            request.session['role'] = request.POST['role']
            return redirect(to=reverse("index"))
        else:
            messages.add_message(request, messages.INFO, '登录失败, 请检查用户名密码')
            return redirect(to=reverse("login"))


class Logout(CheckUserAuthenticatedMixin, View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(request, messages.INFO, '成功退出系统， 您当前已退出。')
        return redirect(to="login")


class MyInfo(CheckUserAuthenticatedMixin, View):
    def get(self, request, *args, **kwargs):
        role = request.session.get('role', None)
        if role not in ROLE_INFO.keys():
            account_role = "未知"
        else:
            account_role = ROLE_INFO[role]
        if role == "student":
            user_obj = Student.objects.filter(user__username=request.user.username).first()
        elif role == "teacher":
            user_obj = Teacher.objects.filter(user__username=request.user.username).first()
        elif role == "admin":
            user_obj = Admin.objects.filter(user__username=request.user.username).first()
        else:
            user_obj = None
        data = {
            'role': account_role,
            'username': request.user.username,
            'create_by': user_obj.create_by.username,
            'create_at': user_obj.create_at
        }
        return render(request=request, template_name="my_info.html", context={'data': data})


class ChangePassword(CheckUserAuthenticatedMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request=request,
                      template_name="change_password.html",
                      context={"messages": get_messages(request)})

    def post(self, request, *args, **kwargs):
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        if confirm_password != new_password or len(new_password) < 8:
            messages.add_message(request, messages.INFO, '修改失败, 两次密码输入不一致或者新密码长度不规范')
            return redirect(to="change_password")
        if not request.user.check_password(old_password):
            messages.add_message(request, messages.INFO, '修改失败, 原密码不正确')
            return redirect(to="change_password")
        try:
            request.user.set_password(new_password)
            request.user.save()
        except Exception:
            messages.add_message(request, messages.INFO, '修改失败')
            return redirect(to="change_password")
        else:
            messages.add_message(request, messages.INFO, '修改成功')
            return redirect(to="login")
