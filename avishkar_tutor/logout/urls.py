from django.conf.urls import url
from . import views

app_name='logout'
urlpatterns = [
url(r'^$',views.logout1, name='logout'),
]