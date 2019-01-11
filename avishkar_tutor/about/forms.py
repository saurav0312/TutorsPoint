from django.contrib.auth.models import User
from django import forms
from contact.models import Teacher,Student
from django.contrib.auth.forms import UserCreationForm

"""class TeacherForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=teacher
        fields=['username','email_id','password']

class StudentForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=student
        fields=['username','reg_no','password']



class TeacherUser(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username','password','email')
"""


class MyForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    email=forms.EmailField(required=True)
    username = forms.CharField(required=True)
    class Meta:
        model=User
        fields=('username','password','email')

        #required_css_class = 'required'

class MyStudentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=('username','password')