from django.db import models as db

class orm_prac(db.Model):
    name=db.CharField(max_length=30)
    surname=db.CharField(max_length=15)
    age=db.IntegerField()
    classroom=db.IntegerField()

    def __str__(self):
        return f'<name:{self.name} Created>'


