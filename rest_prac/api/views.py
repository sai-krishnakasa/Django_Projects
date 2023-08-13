from django.shortcuts import render
from .serial import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render,redirect
from .models import Task
from rest_framework import generics

from rest_framework.viewsets import ViewSet,ModelViewSet

class TaskViewSet(ModelViewSet):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
    
"""
class TaskViewSet(ViewSet):

    def create(self,request):
        serializer=TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def list(self,request):
        tasks=Task.objects.all()
        serializer=TaskSerializer(tasks,many=True)
        return Response(serializer.data)

    def retrieve(self,request,pk):
        try:
            task=Task.objects.get(pk=pk)
        except Exception as e:
            return Response({"status":" "+str(e)})
        serializer=TaskSerializer(task,many=False)
        return Response(serializer.data)

"""

#ListAPIView by default ly only takes a get request 
# if we want to incldue get and post in the same view use CreateApiView along with ListAPIView
#Now get / post are allowed 

"""
class list_tasks(generics.ListAPIView,generics.CreateAPIView):
    #insted of ListAPIView and CreateAPIView 
    #we can use ListCreateAPIView
    '''Provides get and post method handlers.
    Extends: GenericAPIView, ListModelMixin, CreateModelMixin
    '''
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
"""
"""
class update_task(generics.RetrieveUpdateDestroyAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
    lookup_field='id'
"""
"""
class list_tasks2(generics.ListCreateAPIView):
    #insted of ListAPIView and CreateAPIView 
    #we can use ListCreateAPIView
    Provides get and post method handlers.
    Extends: GenericAPIView, ListModelMixin, CreateModelMixin

    queryset=Task.objects.all()
    serializer_class=TaskSerializer

"""
#suppose we need an api for just Update or delete purpose
"""
class update_task(generics.UpdateAPIView,generics.DestroyAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
    lookup_field='id'
"""
"""
#just retrieve and update
class update_task(generics.RetrieveUpdateAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
    lookup_field='id'

"""

"""
@api_view(['GET'])
def list(request):
    tasks=Task.objects.all()
    serial_data=TaskSerializer(tasks,many=True)
    return Response(serial_data.data)
    
    
@api_view(['POST'])
def add(request):
    data=request.data
    serial_data=TaskSerializer(data=data)
    if serial_data.is_valid():
        serial_data.save()
    return redirect('task-list')
        
@api_view(['GET'])
def delete(request,id):
    task=Task.objects.get(pk=id)
    task.delete()
    return redirect('task-list')

@api_view(['POST'])
def update(request,id):
    task=Task.objects.get(pk=id)
    serial_data=TaskSerializer(instance=task,data=request.data)
    if serial_data.is_valid():
        serial_data.save()
    return redirect('task-list')

class fetch_one(generics.RetrieveAPIView):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer
    lookup_field='id'

"""