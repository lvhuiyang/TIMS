# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Admin(models.Model):
    user = models.OneToOneField(User)
    username = models.CharField(verbose_name="用户名", max_length=256, blank=False, null=False, default="")


class Institute(models.Model):
    name = models.CharField(verbose_name="学院名称", max_length=64, default="", blank=False, null=False)
    create_at = models.DateTimeField(verbose_name="创建时间", blank=True, null=True)
    create_by = models.ForeignKey(Admin)


class Major(models.Model):
    name = models.CharField(verbose_name="专业名称", max_length=64, default="", blank=False, null=False)
    institute = models.ForeignKey(Institute)
    create_at = models.DateTimeField(verbose_name="创建时间", blank=True, null=True)
    create_by = models.ForeignKey(Admin)


class Class(models.Model):
    name = models.CharField(verbose_name="班级名称", max_length=64, default="", blank=False, null=False)
    major = models.ForeignKey(Major)
    create_at = models.DateTimeField(verbose_name="创建时间", blank=True, null=True)
    create_by = models.ForeignKey(Admin)


class Student(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=256, blank=False, null=False, default="")
    user = models.OneToOneField(User)
    the_class = models.ForeignKey(Class)
    create_at = models.DateTimeField(verbose_name="创建时间", blank=True, null=True)
    create_by = models.ForeignKey(Admin)


class Teacher(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=256, blank=False, null=False, default="")
    user = models.OneToOneField(User)
    institute = models.ForeignKey(Institute)
    create_at = models.DateTimeField(verbose_name="创建时间", blank=True, null=True)
    create_by = models.ForeignKey(Admin)


class TeacherClassShip(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=256, blank=False, null=False, default="")
    teacher = models.ForeignKey(Teacher)
    the_class = models.ForeignKey(Class)
    create_at = models.DateTimeField(verbose_name="创建时间", blank=True, null=True)
    create_by = models.ForeignKey(Admin)


class Course(models.Model):
    name = models.CharField(verbose_name="课程名称", max_length=64, default="", blank=False, null=False)
    teacher = models.ForeignKey(Teacher)
    create_at = models.DateTimeField(verbose_name="创建时间", blank=True, null=True)


class StudentCourseShip(models.Model):
    student = models.ForeignKey(Student)
    course = models.ForeignKey(Course)
    create_at = models.DateTimeField(verbose_name="创建时间", blank=True, null=True)
    create_by = models.ForeignKey(User)


class Exam(models.Model):
    course = models.ForeignKey(Course)
    student = models.ForeignKey(Student)
    score = models.IntegerField(verbose_name="考试分数", blank=True, null=True)


class MessageLog(models.Model):
    title = models.CharField(verbose_name="消息主题", max_length=256, default="", blank=False, null=False)
    content = models.CharField(verbose_name="消息内容", max_length=256, default="", blank=False, null=False)
    create_at = models.DateTimeField(verbose_name="创建时间", blank=True, null=True)
    create_by = models.ForeignKey(User)


class MessageUserShip(models.Model):
    message = models.ForeignKey(MessageLog)
    user = models.ForeignKey(User)
    have_read = models.BooleanField(verbose_name="是否已读", default=False, blank=False, null=False)
