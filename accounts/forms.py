from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import OTP, User


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "phone_number", "first_name", "last_name")


class OTPForm(forms.ModelForm):
    class Meta:
        model = OTP
        fields = ("pin",)
