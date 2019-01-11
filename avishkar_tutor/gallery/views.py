from django.shortcuts import render
from .models import Student
def gallery(request):
    all_student = Student.objects.all()
    return render(request,'gallery/gallery.html',{'all_student':all_student})
