from django.db import models as db

class story(db.Model):
    name=db.CharField(max_length=100)

    def __str__(self):
        return f'< Story: {self.name} >'
