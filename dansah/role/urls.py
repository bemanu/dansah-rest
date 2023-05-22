from django.urls import path

from .views import Role

urlpatterns = [
    path('', Role.as_view()),
    path('<uuid:pk>', Role.as_view())
]