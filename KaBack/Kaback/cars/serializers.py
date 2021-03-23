from .models import Car
from rest_framework import serializers

class CarSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
        