from django.db import models


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    age = models.IntegerField()
    height = models.DecimalField(decimal_places=1, max_digits=2)

    def __str__(self):
        return self.name
