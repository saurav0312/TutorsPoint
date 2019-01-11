from django.shortcuts import render,render_to_response

def home(request):
    return render(request,'about/home.html',{})

def login(request):
    return render_to_response('about/start_login.html')

def teacher_or_student(request):
    return render_to_response('about/teacher_or_student.html')