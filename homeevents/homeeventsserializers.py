from rest_framework import serializers

from .models import HomeEvent, Event


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class DisplayHomeEventsSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(home_display=True)
        return super(DisplayHomeEventsSerializer, self).to_representation(data)


class FeaturedEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        list_serializer_class = DisplayHomeEventsSerializer
        fields = "__all__"


class HomeEventsSerializer(serializers.ModelSerializer):
    events = FeaturedEventsSerializer(many=True)

    class Meta:
        model = HomeEvent
        fields = "__all__"
