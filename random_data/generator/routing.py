from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/number/', consumers.NumberConsumer.as_asgi()),
]