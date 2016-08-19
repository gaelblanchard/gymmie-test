# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-14 04:37
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rango', '0009_auto_20160813_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='LevelsGraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abslevel', models.FloatField()),
                ('leg', models.FloatField()),
                ('upperarm', models.FloatField()),
                ('lowerarm', models.FloatField()),
                ('back', models.FloatField()),
                ('chest', models.FloatField()),
                ('glutes', models.FloatField()),
                ('neck', models.FloatField()),
                ('overall', models.FloatField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='levelsgraph', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='weightgraph',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 14, 0, 37, 51, 898743)),
        ),
    ]
