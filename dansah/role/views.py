from rest_framework import status, generics
from rest_framework.response import Response

from .models import Role
from .roleserializers import RoleSerializer


class Role(generics.GenericAPIView):
    serializer_class = RoleSerializer
    queryset = Role.objects.all()

    def get(self, request):
        role = Role.objects.all()
        if not role:
            return Response({"status": "No home sliders available"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(role, many=True)
        return Response({
            "status": "success",
            "role": serializer.data
        })

