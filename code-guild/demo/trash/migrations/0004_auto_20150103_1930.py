# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trash', '0003_auto_20150103_0755'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='size',
            field=models.IntegerField(default=48924),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='document',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 3, 19, 29, 4, 168101), auto_now_add=True),
            preserve_default=True,
        ),
    ]
