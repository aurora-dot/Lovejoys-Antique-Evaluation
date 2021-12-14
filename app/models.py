from django.db import models
from accounts.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxLengthValidator

# Create your models here.


class EvaluationRequest(models.Model):
    CONTACT_METHODS = (
        ("E", _("Email")),
        ("P", _("Phone")),
    )

    user = models.ForeignKey(
        User, related_name="evaluation_requests", on_delete=models.CASCADE
    )
    item_description = models.TextField(validators=[MaxLengthValidator(5000)])
    contact_method = models.CharField(max_length=1, choices=CONTACT_METHODS)
