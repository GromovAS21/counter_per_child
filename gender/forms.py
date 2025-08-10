from django import forms
from django.forms import ModelForm

from gender.models import Gender


class GenderUpdateForm(ModelForm):
    """Форма для ввода данных."""
    amount = forms.IntegerField(min_value=0)

    class Meta:
        model = Gender
        fields = ("amount",)
