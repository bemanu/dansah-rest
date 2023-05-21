from rest_framework import generics, status
from rest_framework.response import Response

from .models import HomeActivities, Activities
from .serializers import HomeActivitiesSerializer, ActivitiesSerializer


class HomeActivities(generics.GenericAPIView):
    serializer_class = HomeActivitiesSerializer
    queryset = HomeActivities.objects.all()

    def get(self, request):
        home_activities = HomeActivities.objects.all()
        if not home_activities:
            return Response({"status": "No home sliders available"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(home_activities, many=True)
        return Response({
            "status": "success",
            "home_activities": serializer.data
        })


class Activities(generics.GenericAPIView):
    serializer_class = ActivitiesSerializer
    queryset = Activities.objects.all()

    def get(self, request):
        activities = Activities.objects.all()
        if not activities:
            return Response({"status": "No intro available"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(activities, many=True)
        return Response({
            "status": "success",
            "activities": serializer.data
        })


