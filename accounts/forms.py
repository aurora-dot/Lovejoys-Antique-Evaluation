from django.contrib.auth.forms import UserCreationForm
from .models import User, OTP
from django import forms


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "phone_number", "first_name", "last_name")


class OTPForm(forms.ModelForm):
    class Meta:
        model = OTP
        fields = ("pin",)
