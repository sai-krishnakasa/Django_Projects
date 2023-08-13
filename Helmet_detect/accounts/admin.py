from django.contrib import admin
from .models import MyUser

class MyUserAdmin(admin.ModelAdmin):
    list_display=('email','username','is_staff','is_admin','is_active')
    list_filter=('email','username','is_staff','is_admin','is_active')
    

admin.site.register(MyUser,MyUserAdmin)



