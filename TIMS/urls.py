from django.conf.urls import url
from django.contrib import admin
from application.views import Base, Index, Login, Logout, MyInfo, ChangePassword

app_name = 'tims'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Index.as_view(), name="index"),
    url(r'^base/$', Base.as_view(), name="base"),
    url(r'^login/$', Login.as_view(), name="login"),
    url(r'^logout/$', Logout.as_view(), name="logout"),
    url(r'^my_info/$', MyInfo.as_view(), name="my_info"),
    url(r'^change_password/$', ChangePassword.as_view(), name="change_password"),

]
