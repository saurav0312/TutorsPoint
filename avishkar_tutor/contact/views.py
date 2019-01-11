from django.shortcuts import render

def contact(request):
    return render(request,'contact/contact.html',{})


def student_contact(request):
    return render(request,'contact/student_contact.html',{})
