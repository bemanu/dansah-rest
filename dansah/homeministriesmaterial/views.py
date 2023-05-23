from rest_framework import status, generics
from rest_framework.response import Response

from .models import HomeMinistriesMaterial, MinistriesMaterial
from .serializers import HomeMinistriesMaterialSerializer, MinistriesMaterialSerializer


class HomeMinistriesMaterialView(generics.GenericAPIView):
    serializer_class = HomeMinistriesMaterialSerializer
    queryset = HomeMinistriesMaterial.objects.all()

    def get(self, request):
        home_ministries_material = HomeMinistriesMaterial.objects.all()
        if not home_ministries_material:
            return Response({"status": "No home sliders available"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(home_ministries_material, many=True)
        return Response({
            "status": "success",
            "home_ministries_material": serializer.data
        })


class HomeMinistriesMaterialsDetailView(generics.GenericAPIView):
    serializer_class = HomeMinistriesMaterialSerializer
    queryset = HomeMinistriesMaterial.objects.all()

    def get_home_ministries_material(self, pk):
        try:
            return HomeMinistriesMaterial.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        home_ministries_material = self.get_home_ministries_material(pk=pk)
        if home_ministries_material is None:
            return Response({"status": "fail", "message": f"Home ministries material with Id: {pk} not found"},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(home_ministries_material)
        return Response({"status": "success", "home_ministries_material": serializer.data})


class MinistriesMaterialView(generics.GenericAPIView):
    serializer_class = MinistriesMaterialSerializer
    queryset = MinistriesMaterial.objects.all()

    def get(self, request):
        ministries_material = MinistriesMaterial.objects.all()
        if not ministries_material:
            return Response({"status": "No home ministries material available"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(ministries_material, many=True)
        return Response({
            "status": "success",
            "ministries_material": serializer.data
        })


class MinistriesMaterialsDetailView(generics.GenericAPIView):
    serializer_class = MinistriesMaterialSerializer
    queryset = MinistriesMaterial.objects.all()

    def get_ministries_material(self, pk):
        try:
            return MinistriesMaterial.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        ministries_material = self.get_ministries_material(pk=pk)
        if ministries_material is None:
            return Response({"status": "fail", "message": f"Ministries material with Id: {pk} not found"},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(ministries_material)
        return Response({"status": "success", "ministries_material": serializer.data})
