# Generated by Django 2.2.6 on 2019-10-14 11:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='play',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 14, 11, 15, 9, 122394, tzinfo=utc), null=True, verbose_name='создана'),
        ),
    ]
