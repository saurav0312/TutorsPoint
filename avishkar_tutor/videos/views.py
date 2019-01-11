from django.shortcuts import render,render_to_response
from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView,UpdateView,DeleteView
#from django.core.urlresolvers import reverse_lazy
from django.urls import reverse_lazy
from .models import Video,Course
from django.http import HttpResponse
def new_video_added(request):
    return render(request,'videos/new_video_added.html',{})

def new_course_added(request):
    return render(request,'videos/new_course_added.html',{})

def course1(request):
    all_course = Course.objects.all()
    return render(request, 'videos/videos.html', {'all_course':all_course})

def student_course1(request):
    all_course = Course.objects.all()
    return render(request, 'videos/student_videos.html', {'all_course':all_course})

def video_detail(request, all_course_id):
    #try:
    #    all_member=member.objects.get(pk=member_id)
    #except member.DoesNotExist:
     #   raise Http404("No Such Member")
    all_course=get_object_or_404(Course,pk=all_course_id)
    return render(request, 'videos/video_detail.html', {'all_course':all_course})


def student_video_detail(request, all_course_id):
    #try:
    #    all_member=member.objects.get(pk=member_id)
    #except member.DoesNotExist:
     #   raise Http404("No Such Member")
    all_course=get_object_or_404(Course,pk=all_course_id)
    return render(request, 'videos/student_video_detail.html', {'all_course':all_course})

def search(request):
    if request.method=='POST':
        search_text=request.POST.get('text')
        all_res=Video.objects.filter(name__contains=search_text)
        return render(request, 'videos/res.html', {'all_res': all_res})
    else:
        return render(request, 'videos/search.html', {})


def student_search(request):
    if request.method=='POST':
        search_text=request.POST.get('text')
        all_res=Video.objects.filter(name__contains=search_text)
        return render(request, 'videos/student_res.html', {'all_res': all_res})
    else:
        return render(request, 'videos/student_search.html', {})


class CourseCreate(CreateView):
    model=Course
    fields = ['name']

class VideoCreate(CreateView):
    model=Video
    fields = ['course','name','videofile']

def like_post(request):
    if request.method == 'POST':
        postid = request.POST.get('id')
        post = Video.objects.get(pk=int(postid))
        if post:
            likes = post.likes + 1
            print(likes)
            post.likes = likes
            post.save()

    return render(request, 'videos/student_video_detail.html', {})
