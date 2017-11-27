# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-25 02:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_authors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='book',
            new_name='books',
        ),
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
