# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20160320_1843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genome',
            name='genome',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='genome',
            field=models.ForeignKey(to='main.Genome', default=''),
        ),
    ]
