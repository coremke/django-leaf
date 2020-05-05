# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('leaf', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageNode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True)),
                ('template', models.CharField(blank=True, max_length=255, choices=[])),
                ('path', models.CharField(db_index=True, max_length=255, blank=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', blank=True, to='leaf.PageNode', null=True, on_delete=models.CASCADE)),
            ],
            options={
                'verbose_name': 'page',
            },
        ),
        migrations.AlterUniqueTogether(
            name='pagenode',
            unique_together=set([('slug', 'parent')]),
        ),
    ]
