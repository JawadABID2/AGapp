from django.urls import re_path
from agri.consumers import ChatConsumer
websocket_urlplatterns = [
    re_path('ws/socket-server', ChatConsumer.as_asgi()),
]