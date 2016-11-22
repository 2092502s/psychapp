# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maxi', '0007_subject_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='condition',
            field=models.CharField(null=True, max_length=1),
        ),
    ]
