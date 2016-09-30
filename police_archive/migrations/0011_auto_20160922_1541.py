# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('police_archive', '0010_auto_20160922_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitetext',
            name='content3',
            field=tinymce.models.HTMLField(default='test'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitetext',
            name='content4',
            field=tinymce.models.HTMLField(default='test'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitetext',
            name='content5',
            field=tinymce.models.HTMLField(default='test'),
            preserve_default=False,
        ),
    ]
