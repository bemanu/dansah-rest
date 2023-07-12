from django.urls import path

from .views import (
    QuoteOfTheDayView,
    QuoteOfTheDayDetailView,
    QuoteOfTheDayDetailDateView,
)

urlpatterns = [
    path("", QuoteOfTheDayView.as_view()),
    path("<uuid:pk>", QuoteOfTheDayDetailView.as_view()),
    path("daily/date", QuoteOfTheDayDetailDateView.as_view()),
]
