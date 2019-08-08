# Generated by Django 2.2.4 on 2019-08-08 21:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devbook', '0007_auto_20190808_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='devbook.Post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='time_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 8, 21, 12, 33, 324799)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='time_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 8, 21, 12, 33, 324323)),
        ),
    ]
