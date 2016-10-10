# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('police_archive', '0007_auto_20160504_1055'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='details',
            options={'verbose_name_plural': 'details'},
        ),
    ]
