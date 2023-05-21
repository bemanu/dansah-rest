from django.urls import path

from .views import HomeActivities

urlpatterns = [
    path('', HomeActivities.as_view()),
    path('<str:pk>', HomeActivities.as_view())
]