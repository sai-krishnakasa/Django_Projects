from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    balance = models.IntegerField()

    def __str__(self):
        return self.name
