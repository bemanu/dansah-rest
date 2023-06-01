from django.urls import path

from .views import PowerLivingView, MonthlyPowerLivingView

urlpatterns = [
    path('', PowerLivingView.as_view()),
    path('<uuid:pk>', PowerLivingView.as_view()),
    path('intro', MonthlyPowerLivingView.as_view()),
    path('intro/<uuid:pk>', MonthlyPowerLivingView.as_view())
]
