# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maxi', '0003_auto_20161111_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='endtime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='start_time',
            field=models.DateTimeField(null=True),
        ),
    ]
