# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-10 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('police_archive', '0014_officer_model_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officer',
            name='model_pic',
            field=models.ImageField(default='noimage', upload_to='officer_pictures/'),
        ),
    ]