from django.urls import path

from .views import HomeEventsView, HomeEventsDetailView, EventsView, EventsDetailView

urlpatterns = [
    path("", HomeEventsView.as_view()),
    path("<uuid:pk>", HomeEventsDetailView.as_view()),
    path("events", EventsView.as_view()),
    path("event/<uuid:pk>", EventsDetailView.as_view()),
]
