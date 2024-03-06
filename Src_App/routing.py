# routing.py
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from .consumers import UniqueVisitorsConsumer

application = ProtocolTypeRouter({
    "websocket": AuthMiddlewareStack(
        URLRouter(
            [
                path("ws/unique_visitors/", UniqueVisitorsConsumer.as_asgi()),
            ]
        )
    ),
})
