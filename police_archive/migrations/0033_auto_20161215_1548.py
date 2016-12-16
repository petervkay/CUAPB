# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('police_archive', '0032_auto_20161215_1547'),
    ]

    operations = [
        migrations.RenameField(
            model_name='incident',
            old_name='officers',
            new_name='officer',
        ),
    ]
