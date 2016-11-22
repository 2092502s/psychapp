# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maxi', '0008_auto_20161116_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='confidence',
            field=models.CharField(max_length=1, null=True, blank=True, choices=[('1', 'Not confident at all'), ('2', 'Not very confident'), ('3', 'Unsure'), ('4', 'Quite confident'), ('5', 'Completely confident')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subject',
            name='post0',
            field=models.CharField(max_length=1, null=True, blank=True, choices=[('1', 'None'), ('2', 'Some'), ('3', 'A lot')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='subject',
            name='tutorial_start',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='subject',
            name='post1',
            field=models.CharField(max_length=1, null=True, blank=True, choices=[('1', 'Never'), ('2', 'Occasionally'), ('3', 'Every time')]),
        ),
    ]
