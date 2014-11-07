# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-created'], 'verbose_name': 'Blog Post'},
        ),
        migrations.AddField(
            model_name='blogpost',
            name='votes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
