# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 00:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beltreview', '0002_author_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='beltreview.Users'),
        ),
        migrations.AddField(
            model_name='book',
            name='rating',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='book',
            name='review',
            field=models.TextField(default='review', max_length=255),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=45),
        ),
    ]