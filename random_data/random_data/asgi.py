import os
import django
import logging
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
import generator.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'random_data.settings')
logging.basicConfig(level=logging.DEBUG)
logging.debug('DJANGO_SETTINGS_MODULE set')

django.setup()
logging.debug('Django setup complete')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            generator.routing.websocket_urlpatterns
        )
    ),
})
