# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trash', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 3, 0, 34, 54, 950831), auto_now_add=True),
            preserve_default=True,
        ),
    ]
