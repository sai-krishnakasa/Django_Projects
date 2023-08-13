from django.shortcuts import render
from django.http import HttpResponse
from .tasks import test_func
def test(request):
    test_func()
    return HttpResponse("Hello")