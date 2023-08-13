from django.shortcuts import render
from .models import Person
from django.views.generic.edit import CreateView


class Add(CreateView):
    model = Person
    fields = ("name", "age", "height")
    template_name = "add.html"
    success_url = "/api/"
