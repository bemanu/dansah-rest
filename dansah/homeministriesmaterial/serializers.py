from rest_framework import serializers

from .models import HomeMinistriesMaterial, MinistriesMaterial


class HomeMinistriesMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeMinistriesMaterial
        fields = '__all__'


class MinistriesMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinistriesMaterial
        fields = '__all__'

