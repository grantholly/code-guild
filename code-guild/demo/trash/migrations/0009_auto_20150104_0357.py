# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trash', '0008_auto_20150104_0341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 4, 3, 57, 24, 939663), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to=b''),
            preserve_default=True,
        ),
    ]
