from datetime import datetime
from rest_framework import status, generics
from rest_framework.response import Response

from .models import Devotional
from .serializers import DevotionalSerializer


class Devotion(generics.GenericAPIView):
    serializer_class = DevotionalSerializer
    queryset = Devotional.objects.all()

    def get(self, request):
        devotions = Devotional.objects.all()
        if not devotions:
            return Response({"status": "No devotion available"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(devotions, many=True)
        return Response({
            "status": "success",
            "devotions": serializer.data
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "note": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class DevotionDetail(generics.GenericAPIView):
    serializer_class = DevotionalSerializer
    queryset = Devotional.objects.all()

    def get_devotion(self, pk):
        try:
            return Devotional.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        note = self.get_devotion(pk=pk)
        if note is None:
            return Response({"status": "fail", "message": f"Devotion with Id: {pk} not found"},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(note)
        return Response({"status": "success", "devotion": serializer.data})

    def patch(self, request, pk):
        devotion = self.get_devotion(pk)
        if devotion is None:
            return Response({"status": "fail", "message": f"dDevotion with Id: {pk} not found"},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(
            devotion, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.validated_data['updatedAt'] = datetime.now()
            serializer.save()
            return Response({"status": "success", "note": serializer.data})
        return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        devotion = self.get_devotion(pk)
        if devotion is None:
            return Response({"status": "fail", "message": f"Devotion with Id: {pk} not found"},
                            status=status.HTTP_404_NOT_FOUND)

        devotion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
