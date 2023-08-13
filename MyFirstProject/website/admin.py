from django.contrib import admin
from .models import author, items
# Register your models here.

admin.site.register(items)
admin.site.register(author)