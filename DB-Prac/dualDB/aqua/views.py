from typing import Any, Dict
from django.shortcuts import render
from .models import Person
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView


class Show(TemplateView):
    template_name = "show.html"

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        data = super().get_context_data(**kwargs)
        persons = Person.objects.all()
        print(persons[0]._meta)
        data["persons"] = persons
        return data


class Add(CreateView):
    model = Person
    fields = ("name", "age", "height")
    template_name = "add.html"
    success_url = "/aqua/"
