# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maxi', '0009_auto_20161122_1433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='preq4',
        ),
    ]
