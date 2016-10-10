# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('police_archive', '0011_auto_20160922_1541'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitetext',
            name='content3',
        ),
        migrations.RemoveField(
            model_name='sitetext',
            name='content4',
        ),
        migrations.RemoveField(
            model_name='sitetext',
            name='content5',
        ),
        migrations.AlterField(
            model_name='sitetext',
            name='content1',
            field=models.CharField(max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='sitetext',
            name='content2',
            field=models.TextField(max_length=1000, blank=True),
        ),
    ]
