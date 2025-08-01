from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView

from gender.forms import GenderUpdateForm
from gender.models import Gender


class GenderView(ListView):
    model = Gender
    queryset = Gender.objects.all()


from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


class GenderUpdateView(UpdateView):
    """Прибавление суммы к полу."""

    model = Gender
    form_class = GenderUpdateForm
    success_url = reverse_lazy("gender:home_page")
    template_name = "gender/gender_update.html"


    def form_valid(self, form):
        gender = self.get_object()
        new_value = form.cleaned_data["total"]
        gender.total += new_value
        gender.save()
        # Отправляем обновление через WebSocket
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "gender_updates",
            {
                "type": "gender_update",
                "data": {
                    "id": gender.id,
                    "name": gender.name,
                    "total": gender.total,
                }
            }
        )
        return HttpResponseRedirect(self.get_success_url())


class GenderFullUpdateView(UpdateView):
    """Обновление всей суммы пола."""

    model = Gender
    form_class = GenderUpdateForm
    success_url = reverse_lazy("gender:home_page")
    template_name = "gender/gender_update_full_total.html"

    def form_valid(self, form):
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
        return super().form_valid(form)
