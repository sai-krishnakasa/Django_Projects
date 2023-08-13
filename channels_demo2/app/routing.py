from django.urls import path
from . import consumer

websocket_urlpatterns=[
    path('ws/sc/',consumer.MySyncConsumer.as_asgi(),name='sc'),
    path('ws/asc/',consumer.MyAsyncConsumer.as_asgi(),name='asc'),
]