from django.urls import path
from . import views

urlpatterns = [
    path("display", views.Display.as_view(), name="display"),
    path("create", views.CreateStudents.as_view(), name="create"),
    path("display/<int:pk>", views.Detail.as_view(), name="detail"),
    path("delete/<int:pk>", views.Delete.as_view(), name="delete"),
]
