from .models import Tasks
from rest_framework import serializers

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tasks
        fields='__all__'

    

