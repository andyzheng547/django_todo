# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-18 20:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ('task', 'status'), 'verbose_name_plural': 'todos'},
        ),
    ]
