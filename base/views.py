from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def home(request):
    return render(request, "home.html")


def register(request):

    if request.method == "POST":
        resume = request.FILES.get('student_resume')

        StudentModel.objects.create(
            student_name = request.POST["student_name"],
            student_email = request.POST["student_email"],
            student_number = request.POST["student_number"],
            student_usn = request.POST["student_usn"],
            student_branch = request.POST["student_branch"],
            student_cgpa = request.POST["student_cgpa"],
            student_resume = request.FILES['student_resume'],

        )

        return redirect("login")
    
    return render(request,"register.html")



def login(request):

    data = StudentModel.objects.all()

    return render(request, "login.html",{'data': data})


def dashboard(request):
    return render(request, "dashboard.html")


def admin(request):
    return render(request, "admin.html")


def admin_dashboard(request):
    return render(request, "admin_dashboard.html")


def company_login(request):
    return render(request, "company_login.html")


def company_dashboard(request):

    # Job rules
    min_cgpa = 7.0
    eligible_branches = ['CSE', 'ISE']

    # Filter students based on rules
    students = StudentModel.objects.filter(
        student_cgpa__gte=min_cgpa,
        student_branch__in=eligible_branches
    )

    context = {
        'data': students
    }

    return render(request, 'company_dashboard.html', context)

def job_post(request):
    return render(request, "job_post.html")


def apti(request):
    return render(request, "apti.html")