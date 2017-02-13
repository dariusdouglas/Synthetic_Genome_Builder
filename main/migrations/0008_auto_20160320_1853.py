# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20160320_1848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genome',
            name='user',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='genome_title',
            field=models.ForeignKey(default='', to='main.Genome'),
        ),
        migrations.AlterField(
            model_name='genome',
            name='title',
            field=models.CharField(max_length=256, editable=False),
        ),
    ]
