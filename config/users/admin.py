from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.core.exceptions import ValidationError
from django.db.models import ImageField  
from django.utils.translation import gettext_lazy as _

from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("username", "first_name", "last_name",
                   "email", "avatar", "is_staff", "is_active",)
    list_filter = ("is_staff", "is_active",)
    fieldsets = (
        ("Base", {"fields": ("email", "password", "username")}),
        (_("Permissions"), {"fields": ("is_staff",
                                       "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "username", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )
        }),
    )
    search_fields = ("email",)
    ordering = ("email",)

    # **Дополнительно:**

    # # **1. Регистрация поля "аватар" (если необходимо):**

    # if hasattr(User, "avatar") and isinstance(User._meta.get_field("avatar"), ImageField):
    #     admin.site.register(User.avatar)

    # **2. Настройка разрешений (пример):**

    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return super().has_change_permission(request, obj)

    # **3. Добавление валидации (пример):**

    def clean_email(self, form, field):
        email = super().clean_email(form, field)
        if User.objects.filter(email=email).exists():
            raise ValidationError(_("This email address is already in use."))
        return email

