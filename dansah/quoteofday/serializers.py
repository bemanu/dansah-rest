from rest_framework import serializers

from dansah.quoteofday.models import QuoteOfTheDay


class QuoteOfTheDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteOfTheDay
        fields = '__all__'

