import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_chatapp.settings")

# Initialize Django ASGI application early
django_asgi_app = get_asgi_application()

import chat.consumers  # safe to import after settings are configured

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("ws/chat/<room_name>/", chat.consumers.ChatConsumer.as_asgi()),
        ])
    ),
})
