# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-22 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_auto_20160726_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default='my description'),
            preserve_default=False,
        ),
    ]
