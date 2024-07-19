import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import RandomNumber


class NumberConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        print("WebSocket connection opened")

    async def disconnect(self, close_code):
        print("WebSocket connection closed")

    async def receive(self, text_data):
        print("Received data from client:", text_data)
        latest_number = RandomNumber.objects.latest('timestamp')
        print("Sending data to client:", latest_number.number)
        await self.send(text_data=json.dumps({
            'number': latest_number.number
        }))
