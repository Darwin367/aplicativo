# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-12 03:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cita', '0003_auto_20180211_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citas',
            name='tipo_cita',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tipo.Tipo'),
        ),
    ]
