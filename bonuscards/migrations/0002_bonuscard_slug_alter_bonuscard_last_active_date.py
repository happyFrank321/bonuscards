# Generated by Django 4.1.3 on 2022-12-06 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonuscards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bonuscard',
            name='slug',
            field=models.SlugField(default=1, max_length=16, unique=True, verbose_name='URL'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bonuscard',
            name='last_active_date',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='last_active_date'),
        ),
    ]
