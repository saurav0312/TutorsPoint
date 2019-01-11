from django.conf.urls import url
from . import views

app_name='about'
urlpatterns = [
    url(r'^$',views.about, name='about'),
    url(r'^(?P<member_id>[0-9]+)/$',views.detail, name='detail'),
    url(r'^student/$',views.student_about, name='student_about'),
    url(r'^student/(?P<member_id>[0-9]+)/$',views.student_detail, name='student_detail'),
    url(r'^register/$',views.login, name='register'),
    url(r'^auth/$',views.auth_view, name='auth'),
    url(r'^student_auth/$',views.student_auth_view, name='student_auth'),
    url(r'^invalid/$',views.invalid_login, name='invalid'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^student_signup/$', views.student_signup, name='student_signup'),
    url(r'^student_login/$', views.student_login, name='student_login'),
    #url(r'^teacher_sign/$',views.TeacherFormView.as_view(), name='teacher_sign'),
    #url(r'^student_sign/$',views.StudentFormView.as_view(), name='student_sign'),
    #url(r'^guru_sign/$',views.GuruFormView.as_view(), name='guru_sign'),
]
