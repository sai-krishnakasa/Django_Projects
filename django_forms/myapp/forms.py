from django import forms

class ConatctForm(forms.Form):
    name=forms.CharField()
    email=forms.EmailField(label='E-Mail')
    category=forms.ChoiceField(choices=[('question','Question'),('other','other')])
    subject=forms.CharField(required=False)
    body=forms.CharField(widget=forms.Textarea)

from .models import Snippet

class SnippetForm(forms.ModelForm):

    class Meta:
        model=Snippet
        fields=('name','body')