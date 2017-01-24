# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('police_archive', '0030_auto_20161017_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitetext',
            name='content2',
            field=models.TextField(max_length=500, blank=True),
        ),
    ]
