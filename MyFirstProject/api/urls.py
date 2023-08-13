from django.urls import path
from . import views
urlpatterns=[
    path('get_data',views.getData,name='get_data'),
    path('put_data',views.put_data,name='put_data'),
    path('update_data/<str:pk>',views.update_data,name='put_data'),
    path('delete_data/<str:pk>',views.delete_data,name='put_data'),

]