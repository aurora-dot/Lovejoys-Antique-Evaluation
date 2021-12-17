from random import randint

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class User(AbstractUser):
    email = models.EmailField(_("email address"), unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    phone_number = PhoneNumberField(unique=True, null=False, blank=False)

    REQUIRED_FIELDS = ("email", "first_name", "last_name", "phone_number")

    def __str__(self):
        return self.username


class OTP(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="otp")
    pin = models.CharField(max_length=6, blank=True)

    def save(self, *args, **kwargs):
        self.pin = str(randint(100000, 999999))
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.pin)

    @receiver(post_save, sender=User)  # add this
    def create_otp(sender, instance, created, **kwargs):
        if created:
            OTP.objects.create(user=instance)
