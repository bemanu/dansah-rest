from rest_framework import serializers

from .models import QuoteOfTheDay


class QuoteOfTheDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteOfTheDay
        fields = '__all__'

