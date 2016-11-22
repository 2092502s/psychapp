# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maxi', '0006_auto_20161112_2056'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='condition',
            field=models.CharField(max_length=1, default=0),
            preserve_default=False,
        ),
    ]
