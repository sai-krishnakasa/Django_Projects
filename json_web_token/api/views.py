from django.shortcuts import render
from .serializers import StudentSerailizer
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.
from .models import student

class liststudents(ListAPIView):
    serializer_class=StudentSerailizer
    queryset=student.objects.all()
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

