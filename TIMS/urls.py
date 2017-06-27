from django.conf.urls import url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from application.views import Base, Index, Login, Logout, MyInfo, ChangePassword, \
    InstituteInfoView, MajorInfoView, ClassInfoView, TeacherInfoView, StudentInfoView

app_name = 'tims'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Index.as_view(), name="index"),
    url(r'^base/$', Base.as_view(), name="base"),
    url(r'^login/$', Login.as_view(), name="login"),
    url(r'^logout/$', Logout.as_view(), name="logout"),
    url(r'^my_info/$', MyInfo.as_view(), name="my_info"),
    url(r'^change_password/$', ChangePassword.as_view(), name="change_password"),
    url(r'^info/institute/', InstituteInfoView.as_view(), name="institute_info"),
    url(r'^info/major/', MajorInfoView.as_view(), name="major_info"),
    url(r'^info/class/', ClassInfoView.as_view(), name="class_info"),
    url(r'^info/teacher/', TeacherInfoView.as_view(), name="teacher_info"),
    url(r'^info/student/', StudentInfoView.as_view(), name="student_info"),

]

urlpatterns += staticfiles_urlpatterns()
