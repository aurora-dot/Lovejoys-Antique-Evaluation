from django.contrib.auth.forms import UserCreationForm
from .models import User
from phonenumber_field.formfields import PhoneNumberField


class UserCreationForm(UserCreationForm):
    phone_number = PhoneNumberField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")
