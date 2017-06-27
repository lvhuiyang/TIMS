# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User


class Admin(models.Model):
    class Meta:
        verbose_name = "管理员"

    user = models.OneToOneField(User, verbose_name="指定用户")
    username = models.CharField(verbose_name="用户名", max_length=256, blank=False, null=False, default="")


class Institute(models.Model):
    class Meta:
        verbose_name = "学院"

    name = models.CharField(verbose_name="学院名称", max_length=64, default="", blank=False, null=False)
    create_at = models.DateTimeField(verbose_name="创建时间", blank=True, null=True)
    create_by = models.ForeignKey(Admin, verbose_name="创建者")


class Major(models.Model):
    class Meta:
        verbose_name = "专业"

    name = models.CharField(verbose_name="专业名称", max_length=64, default="", blank=False, null=False)
    institute = models.ForeignKey(Institute, verbose_name="指定学院")
    create_at = models.DateTimeField(verbose_name="创建时间", blank=True, null=True)
    create_by = models.ForeignKey(Admin, verbose_name="创建者")


class Class(models.Model):
    class Meta:
        verbose_name = "班级"

    name = models.CharField(verbose_name="班级名称", max_length=64, default="", blank=False, null=False)
    major = models.ForeignKey(Major, verbose_name="指定专业")
    create_at = models.DateTimeField(verbose_name="创建时间", blank=True, null=True)
    create_by = models.ForeignKey(Admin, verbose_name="创建者")


class Student(models.Model):
    class Meta:
        verbose_name = "学生"

    username = models.CharField(verbose_name="用户名", max_length=256, blank=False, null=False, default="")
    user = models.OneToOneField(User, verbose_name="用户名")
    the_class = models.ForeignKey(Class, verbose_name="指定班级", blank=True, null=True)
    create_at = models.DateTimeField(verbose_name="创建时间", blank=True, null=True)
    create_by = models.ForeignKey(Admin, verbose_name="创建者")


class Teacher(models.Model):
    class Meta:
        verbose_name = "教师"

    username = models.CharField(verbose_name="用户名", max_length=256, blank=False, null=False, default="")
    user = models.OneToOneField(User, verbose_name="指定用户")
    marjor = models.ForeignKey(Major, verbose_name="指定专业", blank=True, null=True)
    create_at = models.DateTimeField(verbose_name="创建时间", blank=True, null=True)
    create_by = models.ForeignKey(Admin, verbose_name="创建者")


class TeacherClassShip(models.Model):
    class Meta:
        verbose_name = "教师班级关系"

    teacher = models.ForeignKey(Teacher, verbose_name="指定教师")
    the_class = models.ForeignKey(Class, verbose_name="指定班级", blank=True, null=True)
    create_at = models.DateTimeField(verbose_name="创建时间", blank=True, null=True)
    create_by = models.ForeignKey(Admin, verbose_name="创建者")


class Course(models.Model):
    class Meta:
        verbose_name = "课程"

    name = models.CharField(verbose_name="课程名称", max_length=64, default="", blank=False, null=False)
    teacher = models.ForeignKey(Teacher, verbose_name="指定教师")
    the_class = models.ForeignKey(Class, verbose_name="指定班级", blank=True, null=True)
    create_at = models.DateTimeField(verbose_name="创建时间", blank=True, null=True)


class Exam(models.Model):
    class Meta:
        verbose_name = "考试"

    course = models.ForeignKey(Course, verbose_name="指定课程")
    student = models.ForeignKey(Student, verbose_name="指定学生")
    score = models.IntegerField(verbose_name="考试分数", blank=True, null=True)
