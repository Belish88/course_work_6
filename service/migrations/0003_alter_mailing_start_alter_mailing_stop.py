# Generated by Django 4.2.7 on 2023-11-14 10:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_alter_log_name_alter_mailing_clients_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='start',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='начало'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='stop',
            field=models.DateTimeField(blank=True, null=True, verbose_name='окончание'),
        ),
    ]
