# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('avatar', models.CharField(max_length=255)),
                ('info', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('category_id', models.IntegerField()),
                ('book_update_time', models.DateTimeField()),
                ('crawl_url', models.CharField(max_length=255)),
                ('status', models.IntegerField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'book',
                'verbose_name': '\u56fe\u4e66',
                'verbose_name_plural': '\u56fe\u4e66',
            },
        ),
    ]
