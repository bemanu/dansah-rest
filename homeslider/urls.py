from django.urls import path

from .views import HomeSliderView, HomeSliderDetailView, IntroView

urlpatterns = [
    path('', HomeSliderView.as_view()),
    path('<uuid:pk>', HomeSliderDetailView.as_view()),
    path('intro', IntroView.as_view()),
]
