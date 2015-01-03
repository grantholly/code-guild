# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trash', '0006_auto_20150103_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='document',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 3, 21, 5, 50, 819625), auto_now_add=True),
            preserve_default=True,
        ),
    ]
