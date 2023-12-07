from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    registration = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to="profile_picture/students/", blank=True, null=True)




class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    teacher_id = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    profile_picture = models.ImageField(upload_to="profile_picture/teachers/", blank=True, null=True)



class ClassRoom(models.Model):
    title = models.CharField(max_length=255)
    students = models.ManyToManyField(Student, null=True)
    teachers = models.ManyToManyField(Teacher, null=True)
    cover_image = models.ImageField(upload_to="cover_image/", blank=True, null=True)
