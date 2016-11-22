# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maxi', '0005_auto_20161112_2047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='consent',
        ),
        migrations.AddField(
            model_name='subject',
            name='consent',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
