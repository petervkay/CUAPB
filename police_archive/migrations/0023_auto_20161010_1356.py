# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-10 18:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('police_archive', '0022_auto_20161010_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officer',
            name='model_pic',
            field=models.ImageField(default='noimage', upload_to='media/police_archive/officer_photos'),
        ),
    ]
