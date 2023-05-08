from django.urls import path
from .views import Devotion, DevotionDetail

urlpatterns = [
    path('', Devotion.as_view()),
    path('<str:pk>', DevotionDetail.as_view())
]