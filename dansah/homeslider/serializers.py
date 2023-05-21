from rest_framework import serializers

from .models import HomeSlider, Intro


class HomeSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeSlider
        fields = '__all__'


class IntroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intro
        fields = '__all__'
