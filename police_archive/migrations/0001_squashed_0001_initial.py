# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-03 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('police_archive', '0001_initial')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_number', models.CharField(max_length=50)),
                ('allegation', models.CharField(max_length=50)),
                ('finding', models.CharField(max_length=50)),
                ('action', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('badge', models.IntegerField()),
                ('department', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='complaint',
            name='officers',
            field=models.ManyToManyField(to=b'police_archive.Officer'),
        ),
    ]
