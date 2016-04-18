# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-15 03:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nProject', '0005_auto_20160415_0327'),
        ('nAsset', '0006_auto_20160315_1205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nasset',
            name='asset_type',
        ),
        migrations.RemoveField(
            model_name='nasset',
            name='path_setup',
        ),
        migrations.RemoveField(
            model_name='nasset',
            name='project_part',
        ),
        migrations.AddField(
            model_name='nasset',
            name='author',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='nasset',
            name='project_hub',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nProject.nProjectHub'),
        ),
        migrations.AddField(
            model_name='nversioncontroler',
            name='asset_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nAsset.nAssetType'),
        ),
        migrations.AddField(
            model_name='nversioncontroler',
            name='hub_pointer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nProject.nProjectHub'),
        ),
        migrations.AlterField(
            model_name='nversioncontroler',
            name='group_name',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='nversioncontroler',
            name='highest_version',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterUniqueTogether(
            name='nversioncontroler',
            unique_together=set([('hub_pointer', 'group_name', 'asset_type')]),
        ),
    ]
