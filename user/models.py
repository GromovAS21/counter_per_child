from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    """Модель Пользователя"""

    username = None
    email = models.EmailField(
        unique=True,
        verbose_name='Email',
        max_length=255,
    )
    avatar = models.ImageField(
        upload_to="users/",
        verbose_name="Аватар",
        blank=True,
        null=True
    )
    token = models.CharField(
        max_length=50,
        verbose_name="Токен",
        blank=True,
        null=True
    )
    first_name = models.CharField(
        max_length=50,
        verbose_name="Имя",
        blank=True,
        null=True,
    )
    second_name = models.CharField(
        max_length=50,
        verbose_name="Фамилия",
        blank=True,
        null=True,
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name="Отчество",
        blank=True,
        null=True
    )
    phone_number = PhoneNumberField(
        region="RU",
        verbose_name="Телефон",
        help_text="Формат: +X XXX XXX XX XX",
        blank=True,
        null=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата регистрации",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def delete(self, *args, **kwargs):
        """
        Удаляет изображение аватара при удалении пользователя
        """
        self.avatar.delete()
        super(User, self).delete(*args, **kwargs)


    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = []