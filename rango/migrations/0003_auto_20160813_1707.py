# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-13 21:07
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rango', '0002_auto_20160806_2210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calculations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height_for_calc', models.IntegerField()),
                ('weight_for_calc', models.IntegerField()),
                ('lunges', models.IntegerField()),
                ('sit_ups', models.IntegerField()),
                ('push_ups', models.IntegerField()),
                ('squats', models.IntegerField()),
                ('calf_raises', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='weightgraph',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 13, 17, 7, 30, 938030)),
        ),
    ]