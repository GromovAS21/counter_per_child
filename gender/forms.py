from django import forms
from django.forms import ModelForm

from gender.models import Gender


class GenderUpdateForm(ModelForm):
    """Форма для ввода данных"""
    amount = forms.IntegerField()

    class Meta:
        model = Gender
        fields = ("amount",)

    def clean_amount(self):
        """Проверка на ввод данных"""
        amount = self.cleaned_data["amount"]
        if amount < 0 or self.cleaned_data["amount"] == 0:
            raise forms.ValidationError("Сумма не может быть меньше или равна 0.")
        return amount