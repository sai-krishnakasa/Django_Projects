from rest_framework.serializers import Serializer,ModelSerializer
from .models import student

class StudentSerailizer(ModelSerializer):
    class Meta:
        model=student
        fields='__all__'