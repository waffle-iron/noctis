# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-10 05:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='nAsset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150)),
                ('object_pointer', models.CharField(default='', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='nObjectType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='nasset',
            name='object_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nAsset.nObjectType'),
        ),
    ]
