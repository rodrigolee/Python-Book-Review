# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 00:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beltreview', '0003_auto_20170301_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='beltreview.Author'),
        ),
    ]