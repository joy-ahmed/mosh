from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'department']



@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'department']



@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']