from rest_framework import serializers
from .models import api_user

class api_serializer(serializers.ModelSerializer):
    class Meta:
        model=api_user
        fields='__all__'