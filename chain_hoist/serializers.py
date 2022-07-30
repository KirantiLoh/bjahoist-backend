from rest_framework import serializers
from .models import ChainHoist, ChainHoistBrand

class ChainHoistSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    class Meta:
        model = ChainHoist
        fields = '__all__'

class ChainHoistBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChainHoistBrand
        fields = ['name',]