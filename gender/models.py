from django.db import models

from user.models import User
import uuid


class GenderChoices(models.TextChoices):
    """Выбор пола"""
    boy = "Мальчик", "мальчик"
    girl = "Девочка", "девочка"


class Gender(models.Model):
    """Модель для главной страницы"""
    id = None
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
        verbose_name="Уникальный идентификатор",
    )
    gender = models.CharField(
        choices=GenderChoices,
        max_length=20,
        verbose_name='Пол',
    )
    amount = models.PositiveIntegerField(
        default=0,
        verbose_name='Сумма',
    )
    image = models.ImageField(
        upload_to="children/",
        verbose_name="Фото",
        blank=True,
        null=True
    )
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="children",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата регистрации",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления",
    )

    def __str__(self):
        return self.gender

    def delete(self, *args, **kwargs):
        """
        Удаляет изображение аватара при удалении карточки
        """
        self.image.delete()
        super(Gender, self).delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Карточка ребенка'
        verbose_name_plural = 'Карточки детей'
        ordering = ("created_at",)
