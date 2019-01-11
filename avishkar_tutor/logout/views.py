from django.shortcuts import render
from django.contrib.auth import login,authenticate,logout

def logout1(request):
    logout(request)
    return render(request,'about/logout.html',{})
