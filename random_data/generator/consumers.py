import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import RandomNumber
from asgiref.sync import sync_to_async


# WebSocket consumer for handling random numbers
class NumberConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Accept WebSocket connection
        await self.accept()
        print("WebSocket connection opened")

    async def disconnect(self, close_code):
        # Log WebSocket disconnection
        print("WebSocket connection closed")

    async def receive(self, text_data):
        # Log received data from client
        print("Received data from client:", text_data)
        # Get the latest generated number from the database
        latest_number = await sync_to_async(RandomNumber.objects.latest)('timestamp')
        print("Sending data to client:", latest_number.number)
        # Send data to the client
        await self.send(text_data=json.dumps({
            'number': latest_number.number
        }))
