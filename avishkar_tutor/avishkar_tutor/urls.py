
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    url(r'^$', views.teacher_or_student,name='teacher_or_student'),
    url(r'^admin/', admin.site.urls),
    url(r'^about/', include('about.urls')),
    url(r'^contact/', include('contact.urls')),
    url(r'^logout/', include('logout.urls')),
    url(r'^gallery/', include('gallery.urls')),
    url(r'^videos/', include('videos.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



