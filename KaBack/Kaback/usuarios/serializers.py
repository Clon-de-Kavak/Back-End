from .models import Usuario as User
from rest_framework import serializers

class UserSerializerModel(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        