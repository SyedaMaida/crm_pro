# accounts/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import Account
from .models import  Owner, Employee,Company
class CustomUserCreationForm(UserCreationForm):
    profile_image = forms.ImageField(required=False)
    class Meta:
        model = Account
        fields = ('email', 'full_name', 'phone','profile_image')
class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Account
        fields = ('email', 'full_name', 'phone',)


class OwnerCreationForm(forms.ModelForm):
    company_name = forms.CharField(max_length=100, help_text="Enter your company name.")

    class Meta:
        model = Owner
        fields = ['username']  # No company_id field here

class EmployeeCreationForm(forms.ModelForm):

    owner_id = forms.ModelChoiceField(queryset=Owner.objects.all(), to_field_name='owner_id', empty_label=None, required=True,label="Owner")
    class Meta:
        model = Employee
        fields = ('username','position','owner_id')
