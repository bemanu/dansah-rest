from django.urls import path

from .views import HomeMinistriesMaterialView

urlpatterns = [
    path("", HomeMinistriesMaterialView.as_view()),
]