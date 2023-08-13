from django.urls import path
from . import views
urlpatterns=[
    path('',views.runcode.as_view(),name='runcode')
]