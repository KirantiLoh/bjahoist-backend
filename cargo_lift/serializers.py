from rest_framework import serializers
from .models import CargoLift

class CargoLiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = CargoLift
        fields = '__all__'