import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

http_asgi = get_asgi_application()

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import gender.routing

application = ProtocolTypeRouter({
    "http": http_asgi,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            gender.routing.websocket_urlpatterns
        )
    ),
})