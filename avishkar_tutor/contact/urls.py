
from django.conf.urls import url
from . import views

app_name='contact'
urlpatterns = [
url(r'^$',views.contact, name='contact'),
url(r'^student/$',views.student_contact, name='student_contact'),
]