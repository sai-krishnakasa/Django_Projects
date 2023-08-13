from typing import Any, Dict
from django.shortcuts import render, redirect
from .models import Students
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods

# from django.  import HttpResponse

from django.views import View
from django.views.generic import (
    TemplateView,
    FormView,
    DetailView,
    DeleteView,
    ListView,
)
from .forms import StudentsCreationForm


class Display(ListView):
    model = Students
    template_name = "main.html"
    context_object_name = "items"
    paginate_by = 2


def Hello(request):
    return JsonResponse("Hello")


class CreateStudents(FormView):
    template_name = "create.html"
    form_class = StudentsCreationForm
    success_url = "display"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Detail(DetailView):
    model = Students
    template_name = "main.html"
    context_object_name = "item"

class Delete(DeleteView):
    model = Students
    template_name = "confirm.html"
    success_url = "/api/display"
    # context_object_name = "Somethig which u wanna access inside the html"
