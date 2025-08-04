from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView

from gender.forms import GenderUpdateForm
from gender.models import Gender, GenderChoices


class GenderView(ListView):
    model = Gender

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context = {
            "boy": Gender.objects.filter(user_id=self.request.user, gender=GenderChoices.boy).first(),
            "girl": Gender.objects.filter(user_id=self.request.user, gender=GenderChoices.girl).first(),
        }
        context_data.update(context)
        return context_data


class GenderUpdateView(UpdateView):
    """Прибавление суммы к полу."""

    model = Gender
    form_class = GenderUpdateForm
    success_url = reverse_lazy("gender:home_page")
    template_name = "gender/gender_update.html"


    def form_valid(self, form):
        child = self.get_object()
        new_value = form.cleaned_data["amount"]
        child.amount += new_value
        child.save()
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "gender_updates",
            {
                "type": "gender_update",
                "data": {
                    "id": child.id,
                    "gender": child.gender,
                    "amount": child.amount,
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
        child = form.save()
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "gender_updates",
            {
                "type": "gender_update",
                "data": {
                    "id": child.id,
                    "gender": child.gender,
                    "amount": child.amount,
                }
            }
        )
        return super().form_valid(form)
