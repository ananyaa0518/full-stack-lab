from django.shortcuts import render


def home(request):

    students = [
        {
            "name": "Rahul Sharma",
            "rollno": "220101",
            "course": "B.Tech Computer Science",
            "semester": 5,
            "cgpa": 8.72
        },
        {
            "name": "Priya Sharma",
            "rollno": "220102",
            "course": "B.Tech Computer Science",
            "semester": 5,
            "cgpa": 7.85
        },
        {
            "name": "Aman Verma",
            "rollno": "220103",
            "course": "B.Tech Information Technology",
            "semester": 5,
            "cgpa": 9.10
        }
    ]

    courses = [
        {
            "name": "Python Programming",
            "credits": 4,
            "faculty": "Dr. Sharma"
        },
        {
            "name": "Database Management Systems",
            "credits": 4,
            "faculty": "Dr. Verma"
        },
        {
            "name": "Web Development",
            "credits": 3,
            "faculty": "Dr. Singh"
        },
        {
            "name": "Blockchain Technology",
            "credits": 3,
            "faculty": "Dr. Kumar"
        }
    ]

    context = {
        "students": students,
        "courses": courses
    }

    return render(request, "student/home.html", context)