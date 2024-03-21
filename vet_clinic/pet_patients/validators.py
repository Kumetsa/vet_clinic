from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_positive_weight(value):
    if value <= 0:
        raise ValidationError(
            _('Weight must be a positive value.'),
            params={'value': value},
        )
