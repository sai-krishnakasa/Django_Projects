from . import views
from django.urls import path,include,re_path

urlpatterns = [


    # path('apiOverview', views.apiOverview,name='api-overview'),
    # path('list', views.list,name='task-list'),
    # path('generic-list', views.list_tasks.as_view(),name='generic-list'),
    # path('generic-list2', views.list_tasks2.as_view(),name='generic-list2'),
    # path('generic-update/<id>/', views.update_task.as_view(),name='generic-update'),
    # path('add', views.add,name='add'),
    # path('fetch-one/<id>/', views.fetch_one.as_view(),name='fetch_one'),
    # # path('delete', views.delete,name='delete'),
    # re_path('^delete/(?P<id>\d+){1,2}/$', views.delete,name='delete'),
    # re_path('^update/(?P<id>\d+){1,2}/$', views.update,name='update'),
]
