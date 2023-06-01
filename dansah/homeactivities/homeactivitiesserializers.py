from rest_framework import serializers

from .models import HomeActivitie, Activitie


class ActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Activitie
        fields = '__all__'


class HomeActivitiesSerializer(serializers.ModelSerializer):
    activities = ActivitiesSerializer(many=True, read_only=True)

    class Meta:
        model = HomeActivitie
        fields = '__all__'
