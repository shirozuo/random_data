from django.urls import path
from . import consumers

# WebSocket URL patterns
websocket_urlpatterns = [
    path('ws/number/', consumers.NumberConsumer.as_asgi()),
]
