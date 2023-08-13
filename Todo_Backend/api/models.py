from django.db import models


class Todos(models.Model):
    todo=models.CharField(max_length=200)
    date_created=models.DateTimeField(auto_now_add=True)
    is_done=models.BooleanField(default=False)
    date_completed=models.DateTimeField(auto_now=True)
