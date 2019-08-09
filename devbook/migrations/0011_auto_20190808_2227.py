# Generated by Django 2.2.4 on 2019-08-08 22:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devbook', '0010_auto_20190808_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 8, 22, 27, 33, 366865)),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 8, 22, 27, 33, 366395)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='profile_image'),
        ),
    ]
