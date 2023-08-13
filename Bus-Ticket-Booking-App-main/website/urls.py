from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [

    path('home',views.home,name='home'),
    path('',views.home,name='home'),
    path('book',views.book,name='book'),
    path('book/<str:id>',views.booking,name='booking'),
    path('user_details',views.user_details,name='user_details')
]
