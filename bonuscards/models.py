from datetime import datetime, timezone

from django.core.exceptions import ValidationError
# check_db.py в качестве проверки, также Celery для автоматичесмко роверки раз в день
# Для ускорения операции лучше пользоваться встроенными средствами бд. Например в постгресе есть функция generate_series
# Создавать много записей нужно с помощью метода QuerySet.bulk_create метод позволяет одним запросом создавать множество объектов.
from django.db import models
from .validators import validate_numbers

CARD_STATUS = (
    ("ACTIVE", "active"),
    ("NOT ACTIVE", "not active"),
    ("DEACTIVE", "deactive"),
)


class BonusCard(models.Model):

    card_series = models.CharField(max_length=4, validators=[validate_numbers],
                                   verbose_name='Серия карты')
    card_number = models.CharField(max_length=12, validators=[validate_numbers],
                                   verbose_name='Номер карты')
    release_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата выпуска', )
    expire_date = models.DateTimeField(auto_now_add=False, verbose_name='Дата окончания', )
    last_active_date = models.DateTimeField(auto_now_add=False, verbose_name='Дата последнего использования', blank=True, null=True,
                                            default=None)
    total_purchases = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=100, choices=CARD_STATUS, default="NOT ACTIVE", verbose_name='Статус')

    class Meta:
        verbose_name = 'Bonus_Card'
        ordering = ('-release_date',)
        unique_together = ('card_series', 'card_number')

    def __str__(self):
        return f'{self.card_series} {self.card_number}'

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.card_series = self.card_series.zfill(4)
        self.card_number = self.card_number.zfill(12)
        super().save(force_insert, force_update, using, update_fields)


class Purchase(models.Model):
    card = models.ForeignKey(BonusCard, related_name='bonuscard', on_delete=models.CASCADE, verbose_name='Карта')
    item = models.CharField(max_length=200, verbose_name='Описание товара')
    total_price = models.IntegerField(verbose_name='Цена покупки')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата покупки',)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        try:
            bcard = BonusCard.objects.get(card_series=self.card.card_series, card_number=self.card.card_number)
        except:
            raise ValidationError('Такой карты не существует')
        if bcard.expire_date < datetime.now(timezone.utc):
            raise ValidationError('Срок действия карты закончен')
        if bcard.status == 'DEACTIVE':
            raise ValidationError('Карта деактивирована')
        bcard.total_purchases += self.total_price
        bcard.status = CARD_STATUS[0][0]
        bcard.last_active_date = datetime.now(timezone.utc)
        bcard.save()
        super().save(force_insert, force_update, using, update_fields)


