from rest_framework import serializers

from .models import HomeEvents, Events


class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'


class HomeEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeEvents
        fields = '__all__'

