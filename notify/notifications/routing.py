from channels.routing import URLRouter
from django.urls  import re_path,path
from django.core.asgi import get_asgi_application
from .consumers import TestConsumer

websocket_urlpatterns=[
    path('',TestConsumer.as_asgi(),name='sc'),
]