from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20)
    email = models.EmailField()
    course = models.CharField(max_length=100)
    semester = models.IntegerField()
    cgpa = models.FloatField()


class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    credits = models.IntegerField()
    faculty = models.CharField(max_length=100)