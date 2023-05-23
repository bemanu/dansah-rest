from django.urls import path

from .views import QuoteOfTheDayView, QuoteOfTheDayDetailView

urlpatterns = [
    path('', QuoteOfTheDayView.as_view()),
    path('<uuid:pk>', QuoteOfTheDayDetailView.as_view())
]
