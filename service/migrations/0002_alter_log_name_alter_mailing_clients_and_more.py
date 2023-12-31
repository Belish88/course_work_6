# Generated by Django 4.2.7 on 2023-11-12 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='name',
            field=models.CharField(max_length=100, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='clients',
            field=models.ManyToManyField(blank=True, null=True, to='service.client', verbose_name='клиенты'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='активна'),
        ),
    ]
