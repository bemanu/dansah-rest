from rest_framework import serializers

from .models import HomeEvent, Event


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'


class HomeEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeEvent
        fields = '__all__'

