"""
ASGI config for dummysocket project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
import sys
sys.path.append("../")
import django
from django.core.asgi import get_asgi_application
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BITSMART.settings')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dummysocket.settings')
django.setup()
# settings.configure()
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from chat.routing import websocket_urlpatterns
# from chat.middleware import TokenAuthMiddleware
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

from django.core.asgi import get_asgi_application


application = get_asgi_application()


application = ProtocolTypeRouter({
  "websocket": AllowedHostsOriginValidator(AuthMiddlewareStack(
      URLRouter(
          websocket_urlpatterns
      )
  )),
})