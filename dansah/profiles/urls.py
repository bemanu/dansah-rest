from django.urls import path

from .views import ProfilesView, ProfilesDetailView

urlpatterns = [
    path('', ProfilesView.as_view()),
    path('<uuid:pk>', ProfilesDetailView.as_view())
]