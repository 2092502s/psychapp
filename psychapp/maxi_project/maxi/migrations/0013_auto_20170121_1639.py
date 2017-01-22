# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maxi', '0012_subject_post3'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='post1',
            field=models.CharField(blank=True, max_length=1, choices=[('1', 'Never'), ('2', 'Rarely'), ('3', 'About half of the time'), ('4', 'Very often'), ('5', 'Every time')], null=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='post3',
            field=models.CharField(blank=True, max_length=1, choices=[('1', 'Very Noisy'), ('2', 'Noisy'), ('3', 'Normal'), ('4', 'Calm'), ('5', 'Very Calm')], null=True),
        ),
    ]
