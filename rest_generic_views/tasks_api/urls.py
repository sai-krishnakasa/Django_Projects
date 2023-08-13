from django.urls import path
from . import views
urlpatterns=[
    path('tasks/',views.CreateTaskView.as_view(),name="task-list"),
    path('task_detail/<id>',views.RetrieveTaskView.as_view(),name="task-detail")
]

