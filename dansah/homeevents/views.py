from rest_framework import status, generics
from rest_framework.response import Response

from .homeeventsserializers import HomeEventsSerializer, EventsSerializer
from .models import HomeEvent, Event


class HomeEventsView(generics.GenericAPIView):
    serializer_class = HomeEventsSerializer
    queryset = HomeEvent.objects.all()

    def get(self, request):
        home_events = HomeEvent.objects.all()
        if not home_events:
            return Response({"status": "No home sliders available"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(home_events, many=True)
        return Response({
            "status": "success",
            "homeevents": serializer.data
        })


class HomeEventsDetailView(generics.GenericAPIView):
    serializer_class = HomeEventsSerializer
    queryset = HomeEvent.objects.all()

    def get_home_events(self, pk):
        try:
            return HomeEvent.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        home_events = self.get_home_events(pk=pk)
        if home_events is None:
            return Response({"status": "fail", "message": f"HomeEvents with Id: {pk} not found"},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(home_events)
        return Response({"status": "success", "homeevents": serializer.data})


class EventsView(generics.GenericAPIView):
    serializer_class = EventsSerializer
    queryset = Event.objects.all()

    def get(self, request):
        events = Event.objects.all()
        if not events:
            return Response({"status": "No events available"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(events, many=True)
        return Response({
            "status": "success",
            "events": serializer.data
        })


class EventsDetailView(generics.GenericAPIView):
    serializer_class = EventsSerializer
    queryset = Event.objects.all()

    def get_events(self, pk):
        try:
            return Event.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        events = self.get_events(pk=pk)
        if events is None:
            return Response({"status": "fail", "message": f"Events with Id: {pk} not found"},
                            status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(events)
        return Response({"status": "success", "events": serializer.data})
