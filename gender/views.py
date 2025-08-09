from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView

from gender.forms import GenderUpdateForm
from gender.models import Gender, GenderChoices


class GenderView(LoginRequiredMixin, ListView):
    model = Gender

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context = {
            "boy": Gender.objects.filter(user_id=self.request.user, gender=GenderChoices.boy).first(),
            "girl": Gender.objects.filter(user_id=self.request.user, gender=GenderChoices.girl).first(),
        }
        context_data.update(context)
        return context_data


class GenderUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Прибавление суммы к полу."""

    model = Gender
    form_class = GenderUpdateForm
    success_url = reverse_lazy("gender:home_page")
    template_name = "gender/gender_update.html"


    def form_valid(self, form):
        child = self.get_object()
        form.save()
        new_value = form.cleaned_data["amount"]
        child.amount += new_value
        child.save()
        user_pk = self.request.user.pk
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"gender_updates_{user_pk}",
            {
                "type": "gender_update",
                "data": {
                    "pk": child.pk,
                    "gender": child.gender,
                    "amount": child.amount,
                }
            }
        )
        return HttpResponseRedirect(self.get_success_url())

    def test_func(self):
        """Проверяем, что пользователь является владельцем объекта."""
        child = self.get_object()
        return self.request.user == child.user_id


class GenderFullUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """Обновление всей суммы пола."""

    model = Gender
    form_class = GenderUpdateForm
    success_url = reverse_lazy("gender:home_page")
    template_name = "gender/gender_update_full_total.html"

    def form_valid(self, form):
        child = form.save()
        user_pk = self.request.user.pk
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"gender_updates_{user_pk}",
            {
                "type": "gender_update",
                "data": {
                    "pk": child.pk,
                    "gender": child.gender,
                    "amount": child.amount,
                }
            }
        )
        return super().form_valid(form)

    def test_func(self):
        """Проверяем, что пользователь является владельцем объекта."""
        child = self.get_object()
        return self.request.user == child.user_id
