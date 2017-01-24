# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('police_archive', '0031_auto_20161017_1021'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='details',
            options={'ordering': ['incident__case_number'], 'verbose_name_plural': 'details'},
        ),
    ]
