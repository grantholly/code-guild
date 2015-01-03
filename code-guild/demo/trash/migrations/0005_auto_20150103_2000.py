# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trash', '0004_auto_20150103_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='file_type',
            field=models.CharField(max_length=4, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='document',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 3, 20, 0, 42, 410338), auto_now_add=True),
            preserve_default=True,
        ),
    ]
