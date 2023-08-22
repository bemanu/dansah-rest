from django.urls import path
from .views import PrayerCityView
    
urlpatterns = [
    path('', PrayerCityView.as_view()),
]