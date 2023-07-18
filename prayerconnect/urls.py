from django.urls import path

from .views import PrayerConnectView
    

urlpatterns = [
    path('', PrayerConnectView.as_view()),
]