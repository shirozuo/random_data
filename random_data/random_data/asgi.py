import os
import django
import logging
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'random_data.settings')
django.setup()

# Import after setting up Django
import generator.routing

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logging.debug('DJANGO_SETTINGS_MODULE set')

# Define application routing for different protocols
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            generator.routing.websocket_urlpatterns
        )
    ),
})
