from django.urls import path

from .views import Intro, HomeSlider

urlpatterns = [
    path('', HomeSlider.as_view()),
    path('<str:pk>', HomeSlider.as_view()),
    path('', Intro.as_view()),
    path('<str:pk>', Intro.as_view())
]