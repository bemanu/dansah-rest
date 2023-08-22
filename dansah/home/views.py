from rest_framework import status, generics
from rest_framework.response import Response
from .models import Home
from .homeserializers import HomeSerializer


# Create your views here.
class HomeView(generics.GenericAPIView):
    serializer_class = HomeSerializer
    queryset = Home.objects.all()

    def get(self, request):
        result = Home.objects.all()
        if not result:
            return Response(
                {"status": "Home Details not available"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.serializer_class(result, many=True)
        return Response({"status": "success", "result": serializer.data})
