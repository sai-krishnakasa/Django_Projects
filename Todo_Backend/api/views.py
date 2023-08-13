from django.shortcuts import render,get_object_or_404
# Create your views here
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import APIView
from .serializer import TodoSerializer
from .models import Todos
from rest_framework.viewsets  import ViewSet,ModelViewSet

class endpoints(APIView):
    def get(self,request):
        context={
            '/list'
            '/create',
            '/delete',
            '/edit',
            '/mark_as_completed'
        }
        return Response(context)
    
class TodosViewset(ModelViewSet):
    serializer_class=TodoSerializer
    queryset=Todos.objects.all()
    
    # def list(self, request):
    #     queryset = Todos.objects.all()
    #     serializer = TodoSerializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, pk=None):
    #     queryset = Todos.objects.all()
    #     item = get_object_or_404(queryset, pk=pk)
    #     serializer = TodoSerializer(item)
    #     return Response(serializer.data)
