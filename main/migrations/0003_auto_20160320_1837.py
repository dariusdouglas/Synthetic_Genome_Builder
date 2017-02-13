# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20160320_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genome',
            name='genome',
            field=models.ForeignKey(to='main.UserProfile', default=''),
        ),
    ]
