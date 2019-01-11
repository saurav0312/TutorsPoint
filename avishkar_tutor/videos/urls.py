from django.conf.urls import url
from . import views

app_name='videos'
urlpatterns = [
    url(r'^$', views.course1, name='course'),
    url(r'^student/$', views.student_course1, name='student_course'),
    url(r'^(?P<all_course_id>[0-9]+)/$',views.video_detail, name='videos_detail'),
    url(r'^student/(?P<all_course_id>[0-9]+)/$',views.student_video_detail, name='student_videos_detail'),
    url(r'^search/$', views.search, name='search'),
    url(r'^student_search/$', views.student_search, name='student_search'),
    url(r'^course_add/$',views.CourseCreate.as_view(),name='course-add'),
    url(r'^videos_add/$',views.VideoCreate.as_view(),name='videos-add'),
    url(r'^course_added$', views.new_course_added, name='course_added'),
    url(r'^video_added$', views.new_video_added, name='video_added'),
    url(r'^like_post/$', views.like_post, name='like_post'),

]