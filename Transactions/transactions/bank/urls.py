from django.urls import path
from . import views

urlpatterns = [path("tran", views.Transaction.as_view(), name="tran")]
