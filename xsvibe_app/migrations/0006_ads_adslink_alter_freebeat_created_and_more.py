# Generated by Django 4.2 on 2023-05-30 08:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('xsvibe_app', '0005_freebeat_beatartistname_alter_freebeat_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='adslink',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='freebeat',
            name='created',
            field=models.TimeField(default=datetime.datetime(2023, 5, 30, 9, 35, 16, 574144)),
        ),
        migrations.AlterField(
            model_name='music',
            name='created',
            field=models.TimeField(default=datetime.datetime(2023, 5, 30, 9, 35, 16, 574144)),
        ),
        migrations.AlterField(
            model_name='video',
            name='created',
            field=models.TimeField(default=datetime.datetime(2023, 5, 30, 9, 35, 16, 574144)),
        ),
    ]
