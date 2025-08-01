from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView

from gender.forms import GenderForm
from gender.models import Gender


class GenderView(ListView):
    model = Gender
    queryset = Gender.objects.all()


from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class GenderUpdateView(UpdateView):
    model = Gender
    form_class = GenderForm
    success_url = reverse_lazy("gender:home_page")

    def form_valid(self, form):
        response = super().form_valid(form)

        # Отправляем обновление через WebSocket
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "gender_updates",
            {
                "type": "gender_update",
                "data": {
                    "id": self.object.id,
                    "name": self.object.name,
                    "total": self.object.total,
                }
            }
        )

        return response
