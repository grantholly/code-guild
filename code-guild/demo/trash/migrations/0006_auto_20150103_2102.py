# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('trash', '0005_auto_20150103_2000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='title',
            new_name='file_name',
        ),
        migrations.AlterField(
            model_name='document',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 3, 21, 2, 11, 667381), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='document',
            name='file_type',
            field=models.CharField(max_length=50, null=True, blank=True),
            preserve_default=True,
        ),
    ]
