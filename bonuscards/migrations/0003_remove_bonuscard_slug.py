# Generated by Django 4.1.3 on 2022-12-08 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bonuscards', '0002_bonuscard_slug_alter_bonuscard_last_active_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bonuscard',
            name='slug',
        ),
    ]
