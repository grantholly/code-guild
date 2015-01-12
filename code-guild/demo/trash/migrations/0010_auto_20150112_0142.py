# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trash', '0009_auto_20150104_0357'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='document',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 12, 1, 42, 35, 371365), auto_now_add=True),
            preserve_default=True,
        ),
    ]
