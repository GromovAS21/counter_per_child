from django.contrib import admin

from user.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """Админка для пользователя."""
    list_display = ("uuid", "email", "is_active", "is_staff")
    search_fields = ("email",)
    list_filter = ("is_active", "is_staff", "is_superuser")



