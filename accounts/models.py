from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext_lazy as _

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    phone_number = PhoneNumberField(null=False, blank=False)

    def __str__(self):
        return self.username
