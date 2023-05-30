from rest_framework import serializers

from .models import SocialMedia, Media


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'


class MediaSerializer(serializers.ModelSerializer):
    social_media = SocialMediaSerializer(many=True, read_only=True)
    class Meta:
        model = Media
        fields = '__all__'

