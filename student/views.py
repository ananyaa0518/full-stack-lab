from django.shortcuts import render
from .models import Student, Course


def home(request):

    students = Student.objects.all()
    courses = Course.objects.all()

    context = {
        "students": students,
        "courses": courses
    }

    return render(request, "student/home.html", context)