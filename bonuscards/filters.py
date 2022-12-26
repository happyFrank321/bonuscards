import django_filters
from django import forms
from bonuscards.models import BonusCard


class CardFilter(django_filters.FilterSet):

    release_date = django_filters.DateFilter('release_date', lookup_expr='icontains', label=('Дата выпуска'), widget=forms.SelectDateWidget())
    expire_date = django_filters.DateFilter('expire_date', lookup_expr='icontains', label=('Дата окончания'), widget=forms.SelectDateWidget())

    class Meta:
        model = BonusCard
        fields = ('card_series', 'card_number', 'release_date', 'expire_date', 'status')