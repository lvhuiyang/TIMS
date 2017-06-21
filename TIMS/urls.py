from django.conf.urls import url
from django.contrib import admin
from application.views import Base, Index, Login

app_name = 'tims'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Index.as_view(), name="index"),
    url(r'^base/$', Base.as_view(), name="base"),
    url(r'^login/$', Login.as_view(), name="login"),

]
