from django.urls import path

from .views import HomeActivitiesView, ActivitiesView, ActivitiesDetailView, HomeActivitiesDetailView

urlpatterns = [
    path('', HomeActivitiesView.as_view()),
    path('<uuid:pk>', HomeActivitiesDetailView.as_view()),
    path('activities/', ActivitiesView.as_view()),
    path('activities/<uuid:pk>', ActivitiesDetailView.as_view())
]
