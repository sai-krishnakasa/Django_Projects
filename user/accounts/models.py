from django.db import models
from django.contrib.auth.models import AbstractUser

class NewUser(AbstractUser):
    age=models.IntegerField(null=True,blank=True)
    nickname=models.CharField(max_length=100,null=True,blank=True)
    phone_no=models.CharField(max_length=10,null=True,blank=True)
