from django.shortcuts import render
from django.http import JsonResponse
from .models import Advocate,Company
from .serializers import AdvocateSerailizer,CompanySerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
# Create your views here.
@api_view(['GET','POST'])
def endpoints(request):
    endpoints=['/advocates','advocates/:username']
    return Response(endpoints)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def advocate_list(request):
    # query=request.GET['query']
    # if query==None:
    #     query=''
    # list=Advocate.objects.filter(username__icontains=query)
    list=Advocate.objects.all()
    s=AdvocateSerailizer(list,many=True)
    return Response(s.data)

@api_view(['GET'])
def advocate_detail(request,username):
    list=Advocate.objects.get(username=username)
    s=AdvocateSerailizer(list,many=False)
    return Response(s.data)


@api_view()
def company_list(request):
    list=Company.objects.all()
    s=CompanySerializer(list,many=True)
    return Response(s.data)

