import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import RandomNumber


class NumberConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        latest_number = RandomNumber.objects.latest('timestamp')
        await self.send(text_data=json.dumps({
            'number': latest_number.number
        }))
