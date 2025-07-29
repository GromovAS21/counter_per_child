from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView

from gender.forms import GenderForm
from gender.models import Gender


class GenderView(ListView):
    model = Gender
    queryset = Gender.objects.all()


class GenderUpdateView(UpdateView):
    model = Gender
    form_class = GenderForm
    success_url = reverse_lazy("gender:home_page")

