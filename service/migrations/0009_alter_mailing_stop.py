# Generated by Django 4.2.7 on 2023-11-16 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_alter_mailing_start_alter_mailing_stop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='stop',
            field=models.DateTimeField(blank=True, verbose_name='окончание'),
        ),
    ]
