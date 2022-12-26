from django import forms
from .validators import  validate_numbers

CARD_ACTIVE_MONTH = (
    ('1', "1 month"),
    ('6', "6 months"),
    ('12', "1 year")
)
CARD_STATUS = (
    ("ACTIVE", "active"),
    ("NOT ACTIVE", "not active"),
    ("DEACTIVE", "deactive"),
)


class BonusCardForm(forms.Form):
    card_series = forms.CharField(max_length=4, validators=[validate_numbers],)
    card_number = forms.CharField(max_length=12, validators=[validate_numbers],)
    release_date = forms.DateTimeField(input_formats=('%Y-%m-%d %H:%M',) )
    expire_date = forms.DateTimeField(input_formats=('%Y-%m-%d %H:%M',) )
    status = forms.ChoiceField(choices=CARD_STATUS)


class CardStatusForm(forms.Form):
    status = forms.ChoiceField(choices=CARD_STATUS, label='Изменить статус')


class CreateMULTCardForm(forms.Form):
    card_series = forms.CharField(max_length=4, validators=[validate_numbers], required=True)
    expires_in = forms.ChoiceField(choices=CARD_ACTIVE_MONTH)
    amount = forms.IntegerField()