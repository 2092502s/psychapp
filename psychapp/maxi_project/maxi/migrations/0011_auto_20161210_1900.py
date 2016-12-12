# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maxi', '0010_remove_subject_preq4'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(null=True, blank=True, max_length=3, choices=[('Aac', 'All A are C'), ('Iac', 'Some A are C'), ('Eac', 'No A are C'), ('Oac', 'Some A are not C'), ('Aca', 'All C are A'), ('Ica', 'Some C are A'), ('Eca', 'No C are A'), ('Oca', 'Some C are not A'), ('NVC', 'No valid conclusion')]),
        ),
    ]
