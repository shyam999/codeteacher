from django.urls import path
from . import views

app_name = 'courses'

urlpatterns = [
    path('language/<slug:language>/', views.CourseListView.as_view(), name='course_list_language'),
    path('<slug:slug>/', views.CourseDetailView.as_view(), name='course_detail'),
]
