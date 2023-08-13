from django.contrib import admin
from .models import MyUser, driver_details,Buses
class MyUserAdmin(admin.ModelAdmin):
    list_display=('email','username','is_staff','is_admin')
    list_filter=('email','username','is_staff','is_admin')
    

admin.site.register(MyUser,MyUserAdmin)
admin.site.register(Buses)
admin.site.register(driver_details)

admin.site.site_header='BUS Ticket App Administration'