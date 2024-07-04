from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
from .models import Owner, Employee, Company
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Account
    list_display = ("email",  "full_name",  "phone", "is_staff", "is_active",)
    list_filter = ("is_staff", "is_active",)
    search_fields = ("email", "username", "full_name")
    ordering = ("full_name",)

    fieldsets = (
        (None, {"fields": ("password",)}),
        ("Personal Info", {"fields": ("email", "full_name",  "phone","profile_image")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions","is_owner","is_employee")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ( "password1", "password2", "email", "full_name", "phone", "is_staff", "is_active"),
        }),
    )
# Register your models here.
# admin.site.register(Account)
admin.site.register(Account, CustomUserAdmin)
admin.site.register(Owner)
admin.site.register(Employee)
admin.site.register(Company)
