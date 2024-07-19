import os
import django
import logging
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'random_data.settings')
django.setup()

# This import must be placed after initializing Django for the correct startup of Daphne
import generator.routing #import after setup

logging.basicConfig(level=logging.DEBUG)
logging.debug('DJANGO_SETTINGS_MODULE set')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            generator.routing.websocket_urlpatterns
        )
    ),
})
