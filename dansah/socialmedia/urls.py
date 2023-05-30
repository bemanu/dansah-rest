from django.urls import path

from .views import MediaView, MediaDetailView, SocialMediaView, \
    SocialMediaDetailView

urlpatterns = [
    path('', MediaView.as_view()),
    path('<uuid:pk>', MediaDetailView.as_view()),
    path('socialmedia', SocialMediaView.as_view()),
    path('socialmedia/<uuid:pk>', SocialMediaDetailView.as_view())
]