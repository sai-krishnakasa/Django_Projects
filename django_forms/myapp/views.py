from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import ConatctForm,SnippetForm
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def contact(request):
    if request.method=='POST':
        form=ConatctForm(request.POST)
        if form.is_valid():
            # name=form.cleaned_data['name']
            #To access a individual field 
            form.save()
    form=ConatctForm()
    return render(request,'form.html',{'form':form})


@csrf_exempt
def snippet_detail(request):
    if request.method=='POST':
        form=SnippetForm(request.POST)
        if form.is_valid():
            print('VALID')
            form.save()
            # name=form.cleaned_data['name']
            #To access a individual field 
            
        else:
            print('Invalid')
    form=SnippetForm()
    return render(request,'form.html',{'form':form})
