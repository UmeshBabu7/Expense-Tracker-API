from django.contrib import admin
from accounts.models.user_models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "phone_number", "is_staff", "created_at")

    list_display_links = ("id", "username")

    list_filter = ("is_staff", "is_superuser", "is_active")

    search_fields = ("username", "email", "phone_number")

    fieldsets = (
        ("Account Info", {"fields": ("username", "password", "email")}),
        ("Personal Info", {"fields": ("phone_number", "bio")}),
        (
            "Permissions",
            {"fields": ("is_active", "is_staff", "is_superuser", "groups")},
        ),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )

    readonly_fields = ("last_login", "date_joined")
