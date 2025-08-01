from django import forms
from django.forms import ModelForm, TextInput

from gender.models import Gender


class GenderUpdateForm(ModelForm):
    """Форма для ввода данных"""
    total = forms.IntegerField()

    class Meta:
        model = Gender
        fields = ("total",)