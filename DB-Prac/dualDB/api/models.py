from django.db import models


class Cls(models.Model):
    name = models.CharField(max_length=100)
    sec = models.CharField(choices=(("A", "A"), ("B", "B"), ("C", "C")), max_length=1)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    cls = models.ForeignKey(Cls, on_delete=models.DO_NOTHING, blank=True, null=True)
    age = models.IntegerField()
    height = models.DecimalField(decimal_places=1, max_digits=2)

    def __str__(self):
        return self.name
