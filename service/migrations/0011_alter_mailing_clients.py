# Generated by Django 4.2.7 on 2023-11-16 09:24

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0010_alter_mailing_stop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='clients',
            field=models.ManyToManyField(default=builtins.all, to='service.client', verbose_name='клиенты'),
        ),
    ]
