from django.urls import path
from . import views
from .views import advocate_list

urlpatterns=[
    path('endpoints',views.endpoints,name='endpoints'),
    path('advocates/',advocate_list,name='advocates'),
    path('advocate_detail/<username>',views.advocate_detail,name='advocate_detail'),
    path('company_list',views.company_list,name='company_list')
]
