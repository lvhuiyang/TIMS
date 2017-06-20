from django.conf.urls import url
from django.contrib import admin
from application.views import Index, Hello, Login

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Index.as_view(), name="index"),
    url(r'^hello/$', Hello.as_view(), name="hello"),
    url(r'^login/$', Login.as_view(), name="hello"),
]
