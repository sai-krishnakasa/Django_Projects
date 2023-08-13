from django.urls  import  path
from . import views
urlpatterns=[ 
    path('list_students',views.liststudents.as_view())
]