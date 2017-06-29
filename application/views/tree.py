from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.messages import get_messages
from application.views import CheckUserAuthenticatedMixin


class TreeView(CheckUserAuthenticatedMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request=request, template_name="tree.html", context={'messages': get_messages(request)})

    def post(self, request, *args, **kwargs):
        type = request.POST['type']
        return HttpResponse(type)
