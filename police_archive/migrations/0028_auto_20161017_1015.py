# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('police_archive', '0027_auto_20161017_0928'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='officer',
            options={'ordering': ['last_name']},
        ),
    ]
