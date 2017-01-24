# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('police_archive', '0026_auto_20161014_1225'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incident',
            old_name='officers2',
            new_name='officers',
        ),
    ]
