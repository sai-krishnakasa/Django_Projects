from django.urls import path
from . import views

urlpatterns=[
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    # path('cookie_login',views.cookie_login,name='cookie'),
    # path('cookie_logout',views.cookie_logout,name='status'),
    # path('home',views.home,name='status'),
    # path('cache',views.cache_view,name='cache_view')
    
]