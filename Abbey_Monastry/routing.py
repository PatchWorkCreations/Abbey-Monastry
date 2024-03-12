# routing.py
from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/visitor_count/$', consumers.VisitorCountConsumer.as_asgi()),
]
