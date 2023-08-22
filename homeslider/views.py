from rest_framework import generics, status
from rest_framework.response import Response

from .homeslidersserializers import HomeSliderSerializer, IntroSerializer
from .models import HomeSlider, Intro


class HomeSliderView(generics.GenericAPIView):
    serializer_class = HomeSliderSerializer
    queryset = HomeSlider.objects.all()

    def get(self, request):
        home_sliders = HomeSlider.objects.all()
        if not home_sliders:
            return Response(
                {"status": "No home sliders available"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.serializer_class(home_sliders, many=True)
        return Response({"status": "success", "result": serializer.data})


class HomeSliderDetailView(generics.GenericAPIView):
    serializer_class = HomeSliderSerializer
    queryset = HomeSlider.objects.all()

    def get_home_slider(self, pk):
        try:
            return HomeSlider.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        home_slider = self.get_ministries_material(pk=pk)
        if home_slider is None:
            return Response(
                {"status": "fail", "message": f"Home slider with Id: {pk} not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.serializer_class(home_slider)
        return Response({"status": "success", "home_slider": serializer.data})


class IntroView(generics.GenericAPIView):
    serializer_class = IntroSerializer
    queryset = Intro.objects.all()

    def get(self, request):
        intro = Intro.objects.all()
        if not intro:
            return Response(
                {"status": "No intro available"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = self.serializer_class(intro, many=True)
        return Response({"status": "success", "result": serializer.data})
