"""educa URL Configuration
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from courses.views import CourseListView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/', include('allauth.urls')),
    path('course/', include('courses.urls')),
    path('students/', include('students.urls')),

    path('', CourseListView.as_view(), name='course_list'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
