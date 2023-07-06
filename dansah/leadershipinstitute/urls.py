from django.urls import path

from .views import CoursesView, CourseDetailView, LeadershipInstituteView

urlpatterns = [
    path('', LeadershipInstituteView.as_view()),
    path("courses/", CoursesView.as_view()),
    path("course/<uuid:pk>", CourseDetailView.as_view()),
]
