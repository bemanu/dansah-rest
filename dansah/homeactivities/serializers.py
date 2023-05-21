from rest_framework import serializers

from .models import HomeActivities, Activities


class HomeActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeActivities
        fields = '__all__'


class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activities
        fields = '__all__'
