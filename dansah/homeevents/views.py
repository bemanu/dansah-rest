
from rest_framework import status, generics
from rest_framework.response import Response

from .models import HomeEvents, Events
from .serializers import HomeEventsSerializer, EventsSerializer


class HomeEvents(generics.GenericAPIView):
    serializer_class = HomeEventsSerializer
    queryset = HomeEvents.objects.all()

    def get(self, request):
        home_events = HomeEvents.objects.all()
        if not home_events:
            return Response({"status": "No home sliders available"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(home_events, many=True)
        return Response({
            "status": "success",
            "home_events": serializer.data
        })


class Events(generics.GenericAPIView):
    serializer_class = EventsSerializer
    queryset = Events.objects.all()

    def get(self, request):
        events = Events.objects.all()
        if not events:
            return Response({"status": "No intro available"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(events, many=True)
        return Response({
            "status": "success",
            "events": serializer.data
        })


