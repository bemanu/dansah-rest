from rest_framework import serializers

from .models import PowerLiving, MonthlyPowerLiving


class MonthlyPowerLivingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyPowerLiving
        fields = '__all__'


class PowerLivingSerializer(serializers.ModelSerializer):
    monthly_power_living = MonthlyPowerLivingSerializer(many=True, read_only=True)

    class Meta:
        model = PowerLiving
        fields = '__all__'
