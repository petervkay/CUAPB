# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('police_archive', '0012_auto_20160922_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitetext',
            name='content1',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='sitetext',
            name='content2',
            field=tinymce.models.HTMLField(),
        ),
    ]
