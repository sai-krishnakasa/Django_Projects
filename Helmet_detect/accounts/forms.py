from random import choices
from django import forms  
from .models import MyUser,Buses
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form  

  
# class CustomUserCreationForm(UserCreationForm):  
#     firstname = forms.CharField(label='firstname', min_length=2, max_length=30)  
#     lastname = forms.CharField(label='lastname', min_length=2, max_length=30)  
#     username = forms.CharField(label='username', min_length=5, max_length=30) 
#     gender=forms.CharField(label='gender') 
#     email = forms.EmailField(label='email')  
#     phone = forms.CharField(label='mobile',max_length=10,min_length=10)  
#     password1 = forms.CharField(label='password', widget=forms.PasswordInput)  
#     password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)  

