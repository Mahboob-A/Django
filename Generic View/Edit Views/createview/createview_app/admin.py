from django.contrib import admin
from .models import Students, Teacher, SchoolStaff
# Register your models here.


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin): 
        list_display = ['id', 'first_name', 'middle_name', 'last_name', 'roll', 'email', 'class_name', 'section']


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin): 
        list_display = ['id', 'name', 'email', 'password']


@admin.register(SchoolStaff)
class SchoolStaffAdmin(admin.ModelAdmin): 
        list_display = ['id', 'name', 'email', 'password']
        