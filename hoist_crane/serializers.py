from rest_framework import serializers
from .models import HoistCrane, HoistCraneBrand

class HoistCraneSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    class Meta:
        model = HoistCrane
        fields = '__all__'

class HoistCraneBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoistCraneBrand
        fields = ['name',]