from rest_framework import status, generics
from rest_framework.response import Response

from .models import Profiles
from .serializers import ProfilesSerializer


class Profiles(generics.GenericAPIView):
    serializer_class = ProfilesSerializer
    queryset = Profiles.objects.all()

    def get(self, request):
        profiles = Profiles.objects.all()
        if not profiles:
            return Response({"status": "No home sliders available"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(profiles, many=True)
        return Response({
            "status": "success",
            "profiles": serializer.data
        })


