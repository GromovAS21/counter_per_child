import json
from channels.generic.websocket import AsyncWebsocketConsumer


class GenderUpdatesConsumer(AsyncWebsocketConsumer):
    """Консьюмер для обновления данных о полах пользователей."""
    async def connect(self):
        """Подключение клиента к каналу."""
        await self.accept()
        await self.channel_layer.group_add("gender_updates", self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("gender_updates", self.channel_name)

    async def receive(self, text_data):
        pass

    async def gender_update(self, event):
        await self.send(text_data=json.dumps(event["data"]))