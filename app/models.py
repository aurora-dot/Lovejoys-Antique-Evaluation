from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import User

# Create your models here.


def validate_image(image):
    file_size = image.file.size

    limit_mb = 5
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max size of file is %s MB" % limit_mb)


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
    image = models.ImageField(
        upload_to="images", null=True, blank=True, validators=[validate_image]
    )
