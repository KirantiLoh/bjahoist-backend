from rest_framework import serializers
from .models import WireRopeHoist, WireRopeHoistBrand

class WireRopeHoistSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    class Meta:
        model = WireRopeHoist
        fields = '__all__'

class WireRopeHoistBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = WireRopeHoistBrand
        fields = ['name',]