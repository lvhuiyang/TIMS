# -*- coding: utf-8 -*-
from django.contrib import admin

from application.models import Admin, Teacher, Student, Class, \
    Course, StudentCourseShip, TeacherClassShip, Major, Exam, MessageLog

admin.site.register(Admin)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Class)
admin.site.register(Course)
admin.site.register(StudentCourseShip)
admin.site.register(TeacherClassShip)
admin.site.register(Major)
admin.site.register(Exam)
admin.site.register(MessageLog)
