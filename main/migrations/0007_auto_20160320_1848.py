# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20160320_1846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='genome',
        ),
        migrations.AddField(
            model_name='genome',
            name='user',
            field=models.ForeignKey(default='', to='main.UserProfile'),
        ),
    ]
