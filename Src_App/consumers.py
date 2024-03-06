# consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Visitor


class UniqueVisitorsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("unique_visitors_group", self.channel_name)

        # Send the initial count on connection
        await self.send(text_data=json.dumps({'count': Visitor.objects.count()}))

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("unique_visitors_group", self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        count = data.get('count', 0)
        await self.update_count({'count': count})

    async def update_count(self, event):
        count = event["count"]

        # Send count to the WebSocket
        await self.send(text_data=json.dumps({'count': count}))
