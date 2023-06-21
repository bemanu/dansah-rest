from rest_framework import status, generics
from rest_framework.response import Response


from .prayerconnectserializers import PrayerConnectSerializer
from .models import PrayerConnect

class PrayerConnectView(generics.GenericAPIView):
    serializer_class = PrayerConnectSerializer
    queryset = PrayerConnect.objects.all()

    def get(self, request):
        result = PrayerConnect.objects.all()
        if not result:
            return Response({"status": "Prayer connect not available"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(result, many=True)
        return Response({
            "status": "success",
            "result": serializer.data
        })