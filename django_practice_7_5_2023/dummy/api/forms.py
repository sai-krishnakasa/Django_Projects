from .models import Students
from django.forms import ModelForm


class StudentsCreationForm(ModelForm):
    class Meta:
        model = Students
        fields = "__all__"
