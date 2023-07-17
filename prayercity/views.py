from rest_framework import status, generics
from rest_framework.response import Response

from .prayercityserializers import PrayerCitySerializer
from .models import PrayerCity

class PrayerCityView(generics.GenericAPIView):
    serializer_class = PrayerCitySerializer
    queryset = PrayerCity.objects.all()

    def get(self, request):
        result = PrayerCity.objects.all()
        if not result:
            return Response({"status": "Prayer city not available"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(result, many=True)
        return Response({
            "status": "success",
            "result": serializer.data
        })