from django.shortcuts import render
from django.http import HttpResponse
from .models import items
# Create your views here.
def index(request):
        dests=items.objects.all()
        return render(request,'index.html',{'item_list':dests})
