from django.urls import path

from .views import Role

urlpatterns = [
    path('', Role.as_view()),
    path('<str:pk>', Role.as_view())
]