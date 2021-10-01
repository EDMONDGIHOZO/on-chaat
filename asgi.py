import os
import django
from channels.auth import AuthMiddlewareStack
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter
import chaat.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'onchaat.settings')
django.setup()


application = ProtocolTypeRouter({
    "http": AsgiHandler(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            chaat.routing.websocket_urlpatterns
        )
    ),
})
