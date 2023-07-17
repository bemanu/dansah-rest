from rest_framework import serializers

from .models import HomeActivity


class HomeActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeActivity
        fields = "__all__"
