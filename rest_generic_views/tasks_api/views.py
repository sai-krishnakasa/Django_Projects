from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.viewsets import ViewSet,ModelViewSet
from .models import Tasks
from rest_framework.response import Response
from .serial import TaskSerializer

class CreateTaskView(generics.CreateAPIView,generics.ListAPIView):
    queryset=Tasks.objects.all()
    serializer_class=TaskSerializer

    # def get_queryset(self):
    #     qs=super().get_queryset()
    #     return qs.filter(is_completed=True)

    def get_serializer_context(self):
        # used to pass context to serializer
        # Ex:serializer=TaskSerializer(queryset,context={"queryset":queryset})
        # and we can access the context in serializer
        context=super().get_serializer_context()
        context["tasks"]=Tasks.objects.all()
        return context
    
    

    
class RetrieveTaskView(generics.RetrieveAPIView):
    queryset=Tasks.objects.all()
    serializer_class=TaskSerializer
    lookup_field='id'

class CreateRetrieveTaskView(ViewSet):
    def list(self,request):
        query_set=Tasks.objects.all()
        serializer=TaskSerializer(query_set,many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer=TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"created"})
        return Response({"Invalid"})

    def update(self,request,pk):
        try:
            obj=Tasks.objects.get(id=pk)
            serializer=TaskSerializer(instance=obj,data=request.data)
            if serializer.is_valid():
                serializer.save()
            return Response({"updated"})
        except Tasks.DoesNotExist:
            return Response("matching query deosn't exist")



        

