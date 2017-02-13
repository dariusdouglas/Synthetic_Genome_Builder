# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_genome_genome_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genome',
            name='file',
            field=models.FileField(upload_to='files/%Y/%m/%d', editable=False),
        ),
        migrations.AlterField(
            model_name='genome',
            name='genome_data',
            field=models.CharField(default='', max_length=255, editable=False),
        ),
    ]
