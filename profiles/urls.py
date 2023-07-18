from django.urls import path

from .views import ProfilesView

urlpatterns = [
    path('', ProfilesView.as_view())
]