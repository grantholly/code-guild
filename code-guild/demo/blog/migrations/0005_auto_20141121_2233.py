# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='comment',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 21, 22, 32, 33, 547908), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='title',
            field=models.CharField(default='test title change me later', max_length=250),
            preserve_default=False,
        ),
    ]
