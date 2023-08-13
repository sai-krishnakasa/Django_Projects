from concurrent.futures.process import _python_exit
from email.policy import default
from enum import unique
from random import choices
from secrets import choice
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.utils import timezone
class MyUserManager(BaseUserManager):
    def create_user(self,email,password=None):
        if not email:
            raise ValueError('email required')
        user=self.model(
            email=self.normalize_email(email),
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user 
    def create_superuser(self,email,password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            password=password,
        )
        user.is_admin=True
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)
        return user 
    

class MyUser(AbstractBaseUser):
    email=models.EmailField(verbose_name='email address',max_length=60,unique=True)
    firstname=models.CharField(max_length=30,default='')
    lastname=models.CharField(max_length=30,default='')
    username=models.CharField(max_length=30)
    phone=models.CharField(max_length=10,verbose_name='contact_no',unique=True)
    gender=models.CharField(max_length=6,blank=False,null=False,choices=(('Male','Male'),('Female','Female')))
    date_joined=models.DateTimeField(verbose_name='date joined',auto_now_add=True)
    last_login=models.DateTimeField(verbose_name='last_login',auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    objects=MyUserManager()
    USERNAME_FIELD='email'
    def __str__(self):
        return self.email
    def has_module_perms(self,app_label):
        return True
    def has_perm(self,perm,obj=None):
        return True

class driver_details(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
    driver_id=models.CharField(max_length=10,primary_key=True)
    mobile=models.CharField(max_length=10,unique=True)
    def __str__(self):
        return self.name
class Buses(models.Model):
    driver_details=models.OneToOneField(
        driver_details,
        on_delete=models.CASCADE,
    )
    origin=models.CharField(max_length=30)
    destination=models.CharField(max_length=30)
    bus_no=models.CharField(max_length=6)
    bus_type=models.CharField(max_length=20,choices=(('Super Luxury-Ac','Super Luxury-Ac '),('Ultra Deluxe-NonAc','Ultra Deluxe-NonAc'),('Super Luxury-NonAc','Super Luxury-NonAc'),('Luxury-Ac','Luxury-Ac '),(' Luxury-NonAc','Luxury-NonAc'),('Garuda-Ac','Garuda-Ac'),('Ultra Deluxe -Ac','Ultra Deluxe-Ac ')))
    seat_type=models.CharField(max_length=20,choices=(('sleeper','sleeper'),('semi-sleeper','semi-sleeper'),('Normal','Normal')))
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()
    fare=models.IntegerField()
    def __str__(self):
        return f'{self.origin} - {self.destination}'
    
    

    