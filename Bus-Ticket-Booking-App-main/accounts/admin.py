from django.contrib import admin
from .models import MyUser,Buses,driver_details,Bookings
class MyUserAdmin(admin.ModelAdmin):
    list_display=('email','username','is_staff','is_admin','is_active')
    list_filter=('email','username','is_staff','is_admin','is_active')
    

admin.site.register(MyUser,MyUserAdmin)
admin.site.site_header='BUS Ticket App Administration'
admin.site.register(Buses)
admin.site.register(driver_details)
admin.site.register(Bookings)

