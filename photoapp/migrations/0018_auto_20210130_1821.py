# Generated by Django 2.0.2 on 2021-01-30 12:51

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('photoapp', '0017_auto_20210130_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 30, 12, 51, 35, 57111, tzinfo=utc)),
        ),
    ]
