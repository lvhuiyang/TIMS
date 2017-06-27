# -*- coding: utf-8 -*-
from django.contrib import admin

from application.models import Admin, Teacher, Student, Class, \
    Course, TeacherClassShip, Major, Exam, Institute

admin.site.register(Admin)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Class)
admin.site.register(Course)
admin.site.register(TeacherClassShip)
admin.site.register(Major)
admin.site.register(Exam)
admin.site.register(Institute)
