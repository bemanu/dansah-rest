from rest_framework import generics, status
from rest_framework.response import Response

from .homeactivitiesserializers import HomeActivitySerializer
from .models import HomeActivity


class HomeActivitiesView(generics.GenericAPIView):
    serializer_class = HomeActivitySerializer
    queryset = HomeActivity.objects.all()

    def get(self, request):
        home_activities = HomeActivity.objects.all()
        if not home_activities:
            return Response(
                {"status": "No home activities available"},
                status=status.HTTP_204_NO_CONTENT,
            )
        serializer = self.serializer_class(home_activities, many=True)
        return Response({"status": "success", "result": serializer.data})
