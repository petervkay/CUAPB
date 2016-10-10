# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('police_archive', '0024_auto_20161010_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='officer',
            name='description',
            field=tinymce.models.HTMLField(blank=True),
        ),
        migrations.AlterField(
            model_name='officer',
            name='model_pic',
            field=models.ImageField(default='noimage', upload_to='police_archive/officer_photos', blank=True),
        ),
    ]
