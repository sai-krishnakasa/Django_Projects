from concurrent.futures.process import _python_exit
from email.policy import default
from enum import unique
from random import choices
from secrets import choice
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.utils import timezone
from django.dispatch import receiver
from django.db.models.signals import post_save



class MyUserManager(BaseUserManager):
    def create_user(self,email,password=None,**kwargs):
        if not email:
            raise ValueError('email required')
        if kwargs:
                first_name=kwargs['first_name']
                last_name=kwargs['last_name']
                user_name=kwargs['user_name']
                phone=kwargs['phone']
                gender=kwargs['gender']
                user=self.model(
                email=self.normalize_email(email),
                firstname=first_name,
                lastname=last_name,
                gender=gender,
                phone=phone,
                username=user_name
                )
                user.set_password(password)
                user.save(using=self._db)
                return user 
        else:
            user=self.model(
                email=self.normalize_email(email))
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
        user.phone=user.pk
        user.save(using=self._db)
        return user 
    

class MyUser(AbstractBaseUser):
    email=models.EmailField(verbose_name='email address',max_length=60,unique=True)
    firstname=models.CharField(max_length=30,default='')
    lastname=models.CharField(max_length=30,default='')
    username=models.CharField(max_length=30)
    phone=models.CharField(max_length=10,verbose_name='contact_no',unique=True)
    gender=models.CharField(max_length=6,blank=False,null=False,choices=(('Male','Male'),('Female','Female')))
    balance=models.IntegerField(default=0)
    profile_pic=models.ImageField(null=True,blank=True,upload_to='media')
    date_joined=models.DateTimeField(verbose_name='date joined',auto_now_add=True)
    last_login=models.DateTimeField(verbose_name='last_login',auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    objects=MyUserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    def __str__(self):
        return self.email
    def has_module_perms(self,app_label):
        return True
    def has_perm(self,perm,obj=None):
        return True
    

# class myTable(models.Model):
#     item=models.CharField(max_length=100)

# class History(models.Model):
#     user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
#     item=models.CharField(max_length=400)

# class driver_details(models.Model):
#     name=models.CharField(max_length=100,blank=False,null=False)
#     driver_id=models.CharField(max_length=10,primary_key=True)
#     mobile=models.CharField(max_length=10,unique=True,blank=False,null=False)
#     def __str__(self):
#         return self.name

# class Bus(models.Model):
#     bus_no=models.CharField(max_length=6)
#     bus_type=models.CharField(max_length=20,choices=(('Super Luxury-Ac','Super Luxury-Ac '),('Ultra Deluxe-NonAc','Ultra Deluxe-NonAc'),('Super Luxury-NonAc','Super Luxury-NonAc'),('Luxury-Ac','Luxury-Ac '),(' Luxury-NonAc','Luxury-NonAc'),('Garuda-Ac','Garuda-Ac'),('Ultra Deluxe -Ac','Ultra Deluxe-Ac ')))
#     seat_type=models.CharField(max_length=20,choices=(('sleeper','sleeper'),('semi-sleeper','semi-sleeper'),('Normal','Normal')))
#     not_booked_seats=models.IntegerField(default=25)
#     def __str__(self):
#         return self.bus_no

# class Buses(models.Model):
#     driver_details=models.ForeignKey(
#         driver_details,
#         on_delete=models.CASCADE,
#         related_name='buses'
#     )
#     origin_choices=(
#         ('Ongole','Ongole'),
#         ('delhi','delhi'),
#         ('rjy','Rajuhmundry'),
#         ('kakinada','kakinada'),
#         ('kolkata','Kolkata'),
#         ('Chennai','Chennai'),
#         ('mumbai','Mumbai'),
#         ('Hyderabad','Hyderabad'),
#         ('Banglore','Banglore'),
#         ('kadapa','kadapa'),
#         ('Noida','Noida'),
#         ('kochi','Kochi'),
#         ('indore','Indore'),
#         ('jammu','Jammu'),
#         ('lucknow','Lucknow'),
#         ('patna','Patna'),
#         ('kanpur','Kanpur'),
#         ('nagpur','Nagpur'),
#         ('nellore','Nellore'),
#     )

#     dest_choices=(
#         ('Ongole','Ongole'),
#         ('Bhadrachalam','Bhadrachalam'),
#         ('chittor','Chittor'),
#         ('ahmedabad','Ahmedabad'),
#         ('vizag','vizag'),
#         ('delhi','delhi'),
#         ('pune','Pune'),
#         ('chittor','Chittor'),
#         ('Banglore','Banglore'),
#         ('rajastan','rajastan'),
#         ('chennai','chennai'),
#         ('Hyderabad','Hyderabad'),
#         ('Nellore','Nellore'),
#         ('bhopal','Bhopal'),
#         ('vijayawada','vijayawada'),
#         ('srinagar','Srinagar'),
#         ('kanpur','Kanpur'),
#         ('patna','Patna'),
#         ('indore','Indore'),
#     )
    

#     origin=models.CharField(max_length=30,choices=sorted(origin_choices))
#     destination=models.CharField(max_length=30,choices=dest_choices)
#     # bus_no=models.CharField(max_length=6)
#     # bus_type=models.CharField(max_length=20,choices=(('Super Luxury-Ac','Super Luxury-Ac '),('Ultra Deluxe-NonAc','Ultra Deluxe-NonAc'),('Super Luxury-NonAc','Super Luxury-NonAc'),('Luxury-Ac','Luxury-Ac '),(' Luxury-NonAc','Luxury-NonAc'),('Garuda-Ac','Garuda-Ac'),('Ultra Deluxe -Ac','Ultra Deluxe-Ac ')))
#     # seat_type=models.CharField(max_length=20,choices=(('sleeper','sleeper'),('semi-sleeper','semi-sleeper'),('Normal','Normal')))
#     # not_booked_seats=models.IntegerField(default=25)
#     bus=models.ForeignKey(
#         Bus,on_delete=models.CASCADE,
#         default='',
#         related_name='bus_details'
#     )
#     start_time=models.DateTimeField()
#     end_time=models.DateTimeField()
#     fare=models.IntegerField()
#     def __str__(self):
#         return f'{self.origin} - {self.destination}'
    


# class Bookings(models.Model):

#     booking_cust_details=models.ForeignKey(
#         MyUser,
#         on_delete=models.CASCADE,
#         related_name='booking_cust'
#     )

#     booking_Bus_details=models.ForeignKey(
#         Buses,
#         on_delete=models.DO_NOTHING,
#         related_name='booking_bus'
#     )
#     no_of_passengers=models.IntegerField()

