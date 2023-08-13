from django.urls import path
from graphene_django.views import GraphQLView
from . import schema
urlpatterns = [
    path('graphi',GraphQLView.as_view(graphiql=True,schema=schema)),
]
