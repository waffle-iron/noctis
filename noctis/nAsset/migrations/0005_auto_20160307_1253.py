# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-07 12:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nAsset', '0004_auto_20160225_0455'),
    ]

    operations = [
        migrations.CreateModel(
            name='nVersionControler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='nasset',
            name='version_group_id',
        ),
        migrations.AddField(
            model_name='nasset',
            name='version_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nAsset.nVersionControler'),
        ),
    ]