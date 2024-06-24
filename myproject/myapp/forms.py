# accounts/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Account

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ('username','email', 'company', 'industry', 'noEmp', 'role', 'name', 'phone')
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Account
        fields = ('username','email', 'company', 'industry', 'noEmp', 'role', 'name', 'phone')
