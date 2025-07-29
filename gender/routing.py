from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/gender-updates/$', consumers.GenderUpdatesConsumer.as_asgi()),
]