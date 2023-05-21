from rest_framework import generics, status
from rest_framework.response import Response

from .models import HomeSlider, Intro
from .serializers import HomeSliderSerializer, IntroSerializer


class HomeSlider(generics.GenericAPIView):
    serializer_class = HomeSliderSerializer
    queryset = HomeSlider.objects.all()

    def get(self, request):
        home_sliders = HomeSlider.objects.all()
        if not home_sliders:
            return Response({"status": "No home sliders available"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(home_sliders, many=True)
        return Response({
            "status": "success",
            "home_sliders": serializer.data
        })

class Intro(generics.GenericAPIView):
    serializer_class = IntroSerializer
    queryset = Intro.objects.all()

    def get(self, request):
        intro = Intro.objects.all()
        if not intro:
            return Response({"status": "No intro available"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(intro, many=True)
        return Response({
            "status": "success",
            "devotions": serializer.data
        })

