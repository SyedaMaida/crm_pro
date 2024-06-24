from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = Account
    list_display = ["email", "username",]

# Register your models here.
# admin.site.register(Account)
admin.site.register(Account, CustomUserAdmin)
