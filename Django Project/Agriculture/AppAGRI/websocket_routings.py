from django.urls import re_path
from AppAGRI.websocket_consumers import ChatConsumer

websocket_urlpatterns = [
    re_path('loraDevice_socket/', ChatConsumer.as_asgi())
]
