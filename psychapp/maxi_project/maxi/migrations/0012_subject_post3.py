# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maxi', '0011_auto_20161210_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='post3',
            field=models.CharField(blank=True, null=True, max_length=1, choices=[('1', 'Noisy'), ('2', 'Normal'), ('3', 'Calm')]),
            preserve_default=True,
        ),
    ]
