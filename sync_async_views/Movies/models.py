from django.db import models as db

# Create your models here.
class movie(db.Model):
    name=db.CharField(max_length=100)

    def __str__(self):
        return f'<Movie: {self.name} >'