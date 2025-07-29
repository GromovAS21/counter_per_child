from django.forms import ModelForm, TextInput

from gender.models import Gender


class GenderForm(ModelForm):
    """Форма для ввода данных"""

    class Meta:
        model = Gender
        fields = ("total",)
        widgets = {
            "total": TextInput(attrs={"placeholder": "Введите общую сумму"}),
        }