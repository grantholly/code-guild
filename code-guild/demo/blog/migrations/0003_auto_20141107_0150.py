# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20141107_0115'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='votes',
            new_name='downvotes',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='upvotes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
