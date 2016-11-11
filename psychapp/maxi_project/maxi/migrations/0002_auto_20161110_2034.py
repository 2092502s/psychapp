# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maxi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='id',
            field=models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True),
        ),
    ]
