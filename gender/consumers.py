import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Gender

class GenderUpdatesConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("gender_updates", self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("gender_updates", self.channel_name)

    async def receive(self, text_data):
        pass  # Мы не ожидаем входящих сообщений от клиента

    async def gender_update(self, event):
        # Отправляем обновленные данные клиенту
        await self.send(text_data=json.dumps(event["data"]))