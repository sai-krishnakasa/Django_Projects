from django.db import models as db

class items(db.Model):
    name=db.CharField(max_length=100)
    img=db.ImageField(upload_to='pics')
    desc=db.TextField()
    price=db.IntegerField()

class author(db.Model):
    author_name=db.CharField(max_length=100)
    country=db.CharField(max_length=20,default='')
    dob=db.DateField()
    dod=db.DateField(blank=True)
    
class user(db.Model):
    name=db.CharField(max_length=100)
    country=db.CharField(max_length=20,default='')
    dob=db.DateField()
    
