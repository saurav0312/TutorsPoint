from django.db import models
from django.http import HttpResponse
from django.urls import resolve
#from django.core.urlresolvers import reverse
from django.urls import reverse
class Course(models.Model):
    name = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('videos:course_added')

    def __str__(self):
        return self.name

class Video(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    videofile= models.FileField(upload_to='files')
    likes = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('videos:video_added')

    def __str__(self):
        return self.name


