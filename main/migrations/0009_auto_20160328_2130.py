# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20160320_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genome',
            name='genome_data',
            field=models.TextField(editable=False, default=''),
        ),
    ]
