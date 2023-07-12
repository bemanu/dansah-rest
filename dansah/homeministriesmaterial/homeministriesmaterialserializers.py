from rest_framework import serializers

from .models import HomeMinistriesMaterial, MinistriesMaterial


class MinistriesMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinistriesMaterial
        fields = '__all__'


class HomeMinistriesMaterialSerializer(serializers.ModelSerializer):
    materials = MinistriesMaterialSerializer(many=True, read_only=True)
    class Meta:
        model = HomeMinistriesMaterial
        fields = '__all__'

