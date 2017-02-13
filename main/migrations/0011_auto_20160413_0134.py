# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20160331_0059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='genome_title',
        ),
        migrations.RemoveField(
            model_name='genome',
            name='genome_data',
        ),
        migrations.AddField(
            model_name='genome',
            name='sequence',
            field=models.TextField(default=datetime.datetime(2016, 4, 13, 1, 34, 26, 798285, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='genome',
            name='file',
            field=models.FileField(upload_to='', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='genome',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='genome',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='genome',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
