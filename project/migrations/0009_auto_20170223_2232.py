# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-02-24 03:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0008_auto_20170223_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='documento',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='tel',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='cedula',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='cel',
            field=models.BigIntegerField(),
        ),
    ]
