from rest_framework import serializers
from .models import PartsAndAccessories, PartsAndAccessoriesBrand

class PartsAndAccessoriesSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    class Meta:
        model = PartsAndAccessories
        fields = '__all__'

class PartsAndAccessoriesBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartsAndAccessoriesBrand
        fields = ['name',]