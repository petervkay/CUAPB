# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('police_archive', '0025_auto_20161010_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officer',
            name='badge',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='officer',
            name='department',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='officer',
            name='description',
            field=tinymce.models.HTMLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='officer',
            name='first_name',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='officer',
            name='last_name',
            field=models.CharField(max_length=80, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='officer',
            name='model_pic',
            field=models.ImageField(default='noimage', null=True, upload_to='police_archive/officer_photos', blank=True),
        ),
    ]
