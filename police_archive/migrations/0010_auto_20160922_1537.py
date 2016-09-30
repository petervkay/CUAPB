# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('police_archive', '0009_sitetext'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sitetext',
            old_name='content',
            new_name='content1',
        ),
        migrations.AddField(
            model_name='sitetext',
            name='content2',
            field=tinymce.models.HTMLField(default='test'),
            preserve_default=False,
        ),
    ]
