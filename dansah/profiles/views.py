from rest_framework import status, generics
from rest_framework.response import Response

from .models import Profiles
from .serializers import ProfilesSerializer


class ProfilesView(generics.GenericAPIView):
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


class ProfilesDetailView(generics.GenericAPIView):
    serializer_class = ProfilesSerializer
    queryset = Profiles.objects.all()

    def get_profiles(self, pk):
        try:
            return Profiles.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        profiles = self.get_profiles(pk=pk)
        if profiles is None:
            return Response({"status": "fail", "message": f"Profile with Id: {pk} not found"},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(profiles)
        return Response({"status": "success", "profiles": serializer.data})
