# Generated by Django 4.1.4 on 2022-12-23 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bonuscards', '0006_alter_bonuscard_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonuscard',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'active'), ('NOT ACTIVE', 'not active'), ('DEACTIVE', 'deactive')], default='NOT ACTIVE', max_length=100, verbose_name='Статус'),
        ),
    ]
