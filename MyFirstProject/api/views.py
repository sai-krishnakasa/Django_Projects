from unicodedata import name
from django.shortcuts import render
from django.urls import is_valid_path
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import response
from api.models import api_user
from website.models import author as items
from django.http import HttpResponse
from .serial import api_serializer
from api import serial

@api_view(['GET'])
def getData(request):
    items=api_user.objects.all()
    serializer=api_serializer(items,many=True)
    return Response(serializer.data)
    

@api_view(['POST'])
def put_data(request):
    serailizer=api_serializer(data=request.data)
    if serailizer.is_valid():
        serailizer.save()
    return HttpResponse('saved')

@api_view(['POST'])
def update_data(request,pk):
    item=api_user.objects.get(id=pk)
    serializer=api_serializer(instance=item,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response('updated')
@api_view(['POST'])
def delete_data(request,pk):
    item=api_user.objects.get(id=pk)
    serializer=api_serializer(instance=item,data=request.data)
    if serializer.is_valid():
        instance=serializer.save()
        instance.delete()
    return Response('deleted')

    
       
    