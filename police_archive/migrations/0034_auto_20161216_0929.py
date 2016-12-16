# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('police_archive', '0033_auto_20161215_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='incident',
            field=models.ForeignKey(to='police_archive.Incident', blank=True),
        ),
        migrations.AlterField(
            model_name='details',
            name='officer',
            field=models.ForeignKey(to='police_archive.Officer', blank=True),
        ),
    ]
