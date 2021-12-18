from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class MixedCaseValidator:
    def validate(self, password, user=None):
        if password.islower():
            raise ValidationError(_("Must contain at least one upper case letter"))
        if password.isupper():
            raise ValidationError(_("Must contain at least one lower case letter"))

    def get_help_text(self):
        return _(
            "Your password must contain at least one lower case and upper case letter"
        )


class SymbolValidator:
    def validate(self, password, user=None):
        if not any(not c.isalnum() for c in password):
            raise ValidationError(_("Must contain at least one symbol"))

    def get_help_text(self):
        return _("Your password must contain one symbol")
