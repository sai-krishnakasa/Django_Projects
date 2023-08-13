from django.db import models

class Tasks(models.Model):
    task_name=models.CharField(max_length=100)
    is_completed=models.BooleanField(default=False)


