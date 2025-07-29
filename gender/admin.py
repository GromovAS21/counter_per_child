from django.contrib import admin

from gender.models import Gender


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "total")