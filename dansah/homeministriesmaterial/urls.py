from django.urls import path

from .views import HomeMinistriesMaterialView, MinistriesMaterialView, MinistriesMaterialsDetailView, \
    HomeMinistriesMaterialsDetailView

urlpatterns = [
    path('', HomeMinistriesMaterialView.as_view()),
    path('<uuid:pk>', HomeMinistriesMaterialsDetailView.as_view()),
    path('ministriesnaterial', MinistriesMaterialView.as_view()),
    path('ministriesnaterial/<uuid:pk>', MinistriesMaterialsDetailView.as_view())
]