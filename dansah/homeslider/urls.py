from django.urls import path

from .views import Intro, HomeSlider

urlpatterns = [
    path('', HomeSlider.as_view()),
    path('<uuid:pk>', HomeSlider.as_view()),
    path('intro', Intro.as_view()),
    path('intro/<uuid:pk>', Intro.as_view())
]