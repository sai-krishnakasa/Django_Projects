from tracemalloc import reset_peak
from django.urls import path,include
from . import views

urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('profile',views.profile,name='profile'),
    path('wallet_bal',views.wallet_bal,name='wallet'),
    path('update_wallet',views.update_wallet,name='update_wallet'),
    # path('booking_details',views.booking_details,name='booking_details'),
    path('admin_desk',views.admin_desk,name='admin_desk'),
    path('edit_profile',views.edit_profile,name='edit_profile'),
    path('session',views.session,name='session'),
    path('forgot_password',views.forgot_password,name='forgot_password'),
    path('reset_password',views.reset_password,name='reset_password'),
    path('verify_otp',views.verify_otp,name='verify_otp'),
    path('history',views.history,name='history'),
    path('contact_us',views.contact_us,name='contact_us'),
    path('admin_desk/buses/<str:id>',views.buses_detail,name='buses_detail'),
    path('admin_desk/buses/delete/<str:id>',views.buses_delete,name='buses_delete'),
    path('admin_desk/drivers/<str:id>',views.driver_detail,name='driver_detail'),
    path('admin_desk/drivers/delete/<str:id>',views.driver_delete,name='driver_delete'),
    path('admin_desk/add_bus',views.add_bus,name='add_bus'),
    path('admin_desk/add_driver',views.add_driver,name='add_driver'),
    path('admin_desk/booking_details',views.booking_details,name='booking_details'),
    # path('admin_desk/send_notification',views.send_ntf,name='send_ntf'),
    path('admin_desk/booking_details/delete_ticket/<str:id>',views.delete_ticket,name='delete_ticket'),
    
]