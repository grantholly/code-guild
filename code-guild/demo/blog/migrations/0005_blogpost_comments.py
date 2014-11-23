# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='comments',
            field=models.ManyToManyField(to='blog.Comment'),
            preserve_default=True,
        ),
    ]
