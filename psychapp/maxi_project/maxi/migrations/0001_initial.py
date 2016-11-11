# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nr_code', models.CharField(max_length=2)),
                ('order_nr', models.CharField(max_length=2)),
                ('answer', models.CharField(null=True, choices=[('A', 'All C are A'), ('B', 'No C are A'), ('C', 'Some C are A'), ('D', 'Some C are not A'), ('E', 'No valid conclusion')], blank=True, max_length=1)),
                ('endtime', models.CharField(null=True, max_length=8)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('consent', models.BooleanField(default=False)),
                ('name', models.CharField(default='Unknown', max_length=500)),
                ('syllogism_order', models.CharField(max_length=500)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('preq1', models.CharField(null=True, choices=[('F', 'Female'), ('M', 'Male'), ('N', 'Not disclosed')], blank=True, max_length=1)),
                ('preq2', models.IntegerField(null=True, blank=True)),
                ('preq3', models.CharField(null=True, choices=[('A', 'Arts & Humanities'), ('B', 'Computing & Engineering'), ('C', 'Social Sciences'), ('D', 'Natural Sciences'), ('E', 'Not at University')], blank=True, max_length=1)),
                ('preq4', models.CharField(null=True, choices=[('A', 'No familiarity at all'), ('B', 'Vaguely familiar'), ('C', 'Very familiar')], blank=True, max_length=1)),
                ('post1', models.CharField(null=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], blank=True, max_length=1)),
                ('post2', models.CharField(null=True, choices=[('1', 'Not familiar'), ('2', 'Vaguely familiar'), ('3', 'Very familiar')], blank=True, max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='question',
            name='subject',
            field=models.ForeignKey(to='maxi.Subject'),
            preserve_default=True,
        ),
    ]
