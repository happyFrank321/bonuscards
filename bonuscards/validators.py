from django.core.exceptions import ValidationError
from datetime import datetime, timezone

def validate_numbers(number):
    if number.isdigit():
        return number
    else:
        raise ValidationError(
            'Форма не должна содержать буквы',
            params={'number': number})


