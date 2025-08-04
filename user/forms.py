from django import forms
from django.contrib.auth.forms import UserCreationForm

from user.models import User


class UserCreateForm(UserCreationForm):
    """Форма регистрации пользователя."""

    class Meta:
        model = User
        fields = ("email", "password1", "password2")

    def  clean_email(self):
        """Валидация на существующий email."""
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Пользователь с таким email уже существует.")
        return email

    def clean_password1(self):
        """Валидация длины пароля."""
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise forms.ValidationError("Пароль должен быть не менее 8 символов.")
        return password1

    def clean_password2(self):
        """Валидация на совпадение паролей."""
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password2 != password1:
            raise forms.ValidationError("Пароли не совпадают.")
        return password2

