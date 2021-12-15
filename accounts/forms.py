from django.contrib.auth.forms import UserCreationForm
from django.forms import ValidationError
from .models import User, Profile
from phonenumber_field.formfields import PhoneNumberField
from django.utils.translation import ugettext_lazy as _


class UserCreationForm(UserCreationForm):
    phone_number = PhoneNumberField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")

    def clean_phone_number(self):
        phone_number = self.cleaned_data["phone_number"]
        if Profile.objects.filter(phone_number=phone_number).exists():
            raise ValidationError(_("Phone number already exists"))
        return phone_number
