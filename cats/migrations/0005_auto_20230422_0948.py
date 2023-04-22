# Generated by Django 3.2 on 2023-04-22 05:48

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0004_auto_20230420_1944'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='changed',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='cat',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 4, 22, 5, 48, 20, 786677, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cat',
            name='is_purebred',
            field=models.BooleanField(default=False),
        ),
    ]
