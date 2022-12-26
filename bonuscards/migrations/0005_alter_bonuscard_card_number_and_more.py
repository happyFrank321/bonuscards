# Generated by Django 4.1.4 on 2022-12-23 14:36

import bonuscards.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonuscards', '0004_alter_bonuscard_options_purchase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonuscard',
            name='card_number',
            field=models.CharField(max_length=12, validators=[bonuscards.validators.validate_numbers], verbose_name='Номер карты'),
        ),
        migrations.AlterField(
            model_name='bonuscard',
            name='card_series',
            field=models.CharField(max_length=4, validators=[bonuscards.validators.validate_numbers], verbose_name='Серия карты'),
        ),
        migrations.AlterField(
            model_name='bonuscard',
            name='expire_date',
            field=models.DateTimeField(verbose_name='Дата окончания'),
        ),
        migrations.AlterField(
            model_name='bonuscard',
            name='last_active_date',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Дата последнего использования'),
        ),
        migrations.AlterField(
            model_name='bonuscard',
            name='release_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата выпуска'),
        ),
        migrations.AlterField(
            model_name='bonuscard',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'active'), ('NOT_ACTIVE', 'not active'), ('DEACTIVE', 'deactive')], default='NOT_ACTIVE', max_length=100, verbose_name='Статус'),
        ),
    ]
