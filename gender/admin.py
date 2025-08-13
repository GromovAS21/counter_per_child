from django.contrib import admin

from gender.models import Gender


@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ("uuid", "gender", "amount", "user_id")
    list_filter = ("gender", "user_id")
    search_fields = ("user_id", )