# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-01-20 12:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0007_respuesta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preguntas',
            name='actividad',
        ),
        migrations.RemoveField(
            model_name='respuesta',
            name='pregunta',
        ),
        migrations.DeleteModel(
            name='Actividades',
        ),
        migrations.DeleteModel(
            name='Preguntas',
        ),
        migrations.DeleteModel(
            name='Respuesta',
        ),
    ]
