# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-02 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('police_archive', '0002_auto_20160502_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='office',
            field=models.CharField(choices=[('CRA', 'Civilian Review Authority'), ('IA', 'Internal Affairs'), ('OPCR', 'Office of Police Conduct Review')], default='OCPR', max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='complaint',
            name='action',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='allegation',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
