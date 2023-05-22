from rest_framework import generics, status
from rest_framework.response import Response

from .models import HomeActivitie, Activitie
from .serializers import HomeActivitiesSerializer, ActivitiesSerializer


class HomeActivitiesView(generics.GenericAPIView):
    serializer_class = HomeActivitiesSerializer
    queryset = HomeActivitie.objects.all()

    def get(self, request):
        home_activities = HomeActivitie.objects.all()
        if not home_activities:
            return Response({"status": "No home activities available"}, status=status.HTTP_204_NO_CONTENT)
        serializer = self.serializer_class(home_activities, many=True)
        return Response({
            "status": "success",
            "home_activities": serializer.data
        })


class HomeActivitiesDetailView(generics.GenericAPIView):
    serializer_class = HomeActivitiesSerializer
    queryset = HomeActivitie.objects.all()

    def get_home_activities(self, pk):
        try:
            return HomeActivitie.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        home_activities = self.get_home_activities(pk=pk)
        if home_activities is None:
            return Response({"status": "fail", "message": f"Home activity with Id: {pk} not found"},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(home_activities)
        return Response({"status": "success", "home_activities": serializer.data})


class ActivitiesView(generics.GenericAPIView):
    serializer_class = ActivitiesSerializer
    queryset = Activitie.objects.all()

    def get(self, request):
        activities = Activitie.objects.all()
        if not activities:
            return Response({"status": "No activities available"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(activities, many=True)
        return Response({
            "status": "success",
            "activities": serializer.data
        })


class ActivitiesDetailView(generics.GenericAPIView):
    serializer_class = ActivitiesSerializer
    queryset = Activitie.objects.all()

    def get_activities(self, pk):
        try:
            return Activitie.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        activities = self.get_activities(pk=pk)
        if activities is None:
            return Response({"status": "fail", "message": f"Activities with Id: {pk} not found"},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(activities)
        return Response({"status": "success", "activities": serializer.data})
