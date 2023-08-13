from django.db import models


class Students(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    sec = models.CharField(choices=(("A", "A"), ("B", "B"), ("C", "C")), max_length=2)
    dept = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
