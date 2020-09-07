# Generated by Django 3.0.3 on 2020-09-07 07:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0017_auto_20200907_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='start_day',
            field=models.DateField(default=datetime.datetime(2020, 8, 31, 7, 53, 10, 517205)),
        ),
        migrations.AlterField(
            model_name='registration',
            name='day_registered',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 9, 7, 7, 53, 10, 530604)),
        ),
        migrations.AlterField(
            model_name='registration',
            name='timestamp',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 7, 7, 53, 10, 530546, tzinfo=utc)),
        ),
    ]
