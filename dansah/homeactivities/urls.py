from django.urls import path

from .views import HomeActivitiesView

urlpatterns = [
    path("", HomeActivitiesView.as_view()),
]
