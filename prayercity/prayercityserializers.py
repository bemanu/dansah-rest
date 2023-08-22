from rest_framework import serializers

from .models import PrayerCity

class PrayerCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PrayerCity
        fields = '__all__'

