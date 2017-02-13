# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20160328_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='genome',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 3, 31, 0, 59, 5, 58211, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='genome',
            name='updated',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2016, 3, 31, 0, 59, 25, 5778, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='genome',
            name='file',
            field=models.FileField(upload_to='files/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='genome',
            name='title',
            field=models.CharField(max_length=256),
        ),
    ]
