# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maxi', '0002_auto_20161110_2034'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='start_time',
            field=models.CharField(null=True, max_length=8),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.IntegerField(null=True),
        ),
    ]
