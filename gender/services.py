from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def send_ws_message(user_pk, value, amount):
    """Отправка сообщения в WebSocket."""
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        f"gender_updates_{user_pk}",
        {
            "type": "gender_update",
            "data": {
                "pk": value.pk,
                "gender": value.gender,
                "amount": amount,
            }
        }
    )