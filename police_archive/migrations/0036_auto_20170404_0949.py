# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 14:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('police_archive', '0035_incident_department'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='incident',
            unique_together=set([('case_number', 'department')]),
        ),
        migrations.AlterUniqueTogether(
            name='officer',
            unique_together=set([('first_name', 'last_name', 'badge', 'department')]),
        ),
    ]
