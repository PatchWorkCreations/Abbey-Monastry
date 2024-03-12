# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer

from Src_App.models import Visitor


class VisitorCountConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        # Send the initial count to the client upon connection
        await self.send_visitor_count()

        # Add the current WebSocket consumer to a group
        await self.channel_layer.group_add("visitor_group", self.channel_name)

    async def disconnect(self, close_code):
        # Remove the consumer from the group when disconnected
        await self.channel_layer.group_discard("visitor_group", self.channel_name)

    async def send_visitor_count(self, event=None):
        # Send the current visitor count to the client
        unique_visitors_count = Visitor.objects.values('ip_address').distinct().count()
        await self.send(text_data=json.dumps({'count': unique_visitors_count}))
