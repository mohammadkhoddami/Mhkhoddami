import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_phone_number(value):
    if not re.match(r'^09\d{9}$', value):
        raise ValidationError(_('Phone Number Must Be String')) #TODO User get text lazy for tarnslation

    