# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 04:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beltreview', '0008_auto_20170302_1509'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author',
            new_name='authors',
        ),
    ]
