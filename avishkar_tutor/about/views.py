from django.shortcuts import get_object_or_404,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render, render_to_response
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
from .models import Member
from django.views.generic import View
from .forms import MyForm,MyStudentForm
from django.template import RequestContext
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib.auth.models import User

def about(request):
    all_member=Member.objects.all()
    context={'all_member':all_member}
    return render(request, 'about/index.html', context)


def detail(request, member_id):
    #try:
    #    all_member=member.objects.get(pk=member_id)
    #except member.DoesNotExist:
     #   raise Http404("No Such Member")
    all_member=get_object_or_404(Member,pk=member_id)
    return render(request, 'about/detail.html', {'all_member':all_member})

def student_about(request):
    all_member=Member.objects.all()
    context={'all_member':all_member}
    return render(request, 'about/student_index.html', context)


def student_detail(request, member_id):
    #try:
    #    all_member=member.objects.get(pk=member_id)
    #except member.DoesNotExist:
     #   raise Http404("No Such Member")
    all_member=get_object_or_404(Member,pk=member_id)
    return render(request, 'about/student_detail.html', {'all_member':all_member})


def login(request):
    return render_to_response('about/registration_form.html')

def student_login(request):
    return render_to_response('about/start_login.html')


def invalid_login(request):
    return render_to_response('about/invalid_login.html')

def auth_view(request):
    username=request.POST.get('username','')
    password = request.POST.get('password', '')
    email=request.POST.get('email','')
    is_there=get_object_or_404(User,email=email)
    if is_there:
        user=auth.authenticate(username=username,password=password,email=email)

        if user is not None:
            auth.login(request,user)
            return redirect('about:about')
        else:
            return redirect('about:invalid')
    else:
        return redirect('about:invalid')


def student_auth_view(request):
    username=request.POST.get('username','')
    password = request.POST.get('password', '')
    email=request.POST.get('email','')
    user=auth.authenticate(username=username,password=password,email=email)

    if user is not None:
        auth.login(request,user)
        return redirect('about:student_about')
    else:
        return redirect('about:invalid')

def logout(request):
    auth.logout(request)
    return render_to_response(request,'about/logout.html')


def signup(request):
    if request.method=='POST':
        #form=UserCreationForm(request.POST)
        form=MyForm(request.POST)

        if form.is_valid():
            user=form.save(commit=False)
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            email=request.POST.get('email','')
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password,email=email)
            login(user)
            return render(request, 'about/home.html',{})
        else:
            return render(request, 'about/home.html', {})
    else:
        #form=UserCreationForm()
        form=MyForm()
        return render(request, 'about/signup.html', {'form': form})

def student_signup(request):
    if request.method=='POST':
        #form=UserCreationForm(request.POST)
        form=MyStudentForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            email = request.POST.get('email', '')
            user.set_password(password)
            user.save()
            user = authenticate(username=username, password=password,email=email)
            login(user)
            return render(request, 'about/student_home.html',{})
        else:
            return render(request, 'about/student_home.html', {})
    else:
        #form=UserCreationForm()
        form=MyStudentForm()
        return render(request, 'about/student_signup.html', {'form': form})



#class TeacherCreate(CreateView):
 #   model=teacher
  #  fields = ['username','password','email_id']

#class StudentCreate(CreateView):
 #   model=student
  #  fields = ['username','password','email_id','reg_no']


"""class TeacherFormView(View):
    form_class=TeacherForm
    template_name='about/registration.html'
    #display blank form
    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    #process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user=form.save(commit=False)
            #username=form.cleaned_data['username']
            #password = form.cleaned_data['password']
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user.save()

            user=authenticate(username=username,password=password)
            login(user)
            return redirect('about:about')

        return  render(request,self.template_name,{'form':form})


class StudentFormView(View):
    form_class=StudentForm
    template_name='about/registration.html'
    #display blank form
    def get(self,request):
        form=self.form_class(None)
        return render(request,self.template_name,{'form':form})

    #process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user=form.save(commit=False)
            #username=form.cleaned_data['username']
            #password = form.cleaned_data['password']
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user.save()

            user=authenticate(username=username,password=password)
            login(user)
            return redirect('about:student_about')

        return  render(request,self.template_name,{'form':form})


class GuruFormView(View):
    teacheruser=TeacherUser

    template_name='about/registration.html'
    #display blank form
    def get(self,request):
        teacheruser=self.teacheruser(None)
        return render(request,self.template_name,{'teacheruser':teacheruser})

    #process form data
    def post(self, request):
        teacheruser = self.teacheruser(request.POST)

        if teacheruser.is_valid():
            teacheruser.save()
            #username=form.cleaned_data['username']
            #password = form.cleaned_data['password']
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            email = request.POST.get('email', '')
            user=authenticate(username=username,password=password,email=email)

            login(user)
            return redirect('about:about')

        return  render(request,self.template_name,{'teacheruser':teacheruser})
"""





















