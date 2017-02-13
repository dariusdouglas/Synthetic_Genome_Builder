# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20160320_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='genome',
            name='genome_data',
            field=models.CharField(default='', max_length=255),
        ),
    ]
