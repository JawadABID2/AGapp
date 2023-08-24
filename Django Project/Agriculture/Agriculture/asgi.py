"""
ASGI config for Agriculture project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from AppAGRI.mqtt_consumer import MqttChannelConsumer
from AppAGRI.websocket_routings import websocket_urlpatterns
from channels.auth import AuthMiddlewareStack

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Agriculture.settings')

# application = get_asgi_application()

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket' : AuthMiddlewareStack(URLRouter(websocket_urlpatterns)),
})

mqtt_app = ProtocolTypeRouter({
    'mqtt': MqttChannelConsumer.as_asgi(),
})
