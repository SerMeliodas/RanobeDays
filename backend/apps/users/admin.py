from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User


class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = ("username", "email", "is_staff", "is_superuser")
    list_filter = ("username", "email", "is_staff", "is_superuser")
    fieldsets = (
        (None, {"fields": ("public_username",
         "username", "email", "avatar", "password")}),
        ("Permisions", {"classes": ("collapse",),
                        "fields": ("is_staff", "is_active",
                                   "groups", "user_permissions"),
                        })
    )
    add_fieldsets = (
        (None, {"classes": ("wide",),
                "fields": ("username", "email", "password1", "password2",
                           "is_staff", "is_active", "groups",
                           "user_permissions")
                }),
    )
    search_fields = ("username", "email")
    ordering = ("username",)


admin.site.register(User, UserAdmin)
