# Generated by Django 2.2.4 on 2019-08-11 22:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devbook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 11, 22, 40, 39, 990385)),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 11, 22, 40, 39, 989804)),
        ),
    ]
