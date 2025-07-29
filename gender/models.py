from django.db import models

class GenderChoices(models.TextChoices):
    """Выбор пола"""
    boy = "Мальчик", "мальчик"
    girl = "Девочка", "девочка"


class Gender(models.Model):
    """Модель для главной страницы"""
    name = models.CharField(
        choices=GenderChoices,
        max_length=20,
        unique=True,
        verbose_name='Пол',
    )
    total = models.PositiveIntegerField(
        default=0,
        verbose_name='Сумма',
    )
    photo = models.ImageField(
        upload_to="",
        verbose_name="Фото",
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        """
        Удаляет изображение аватара при удалении пользователя
        """
        self.photo.delete()
        super(Gender, self).delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Пол'
        verbose_name_plural = 'Пола'
        ordering = ("id",)
