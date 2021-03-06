# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 02:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternPrjPawAllActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(blank=True, max_length=64, null=True)),
                ('opr_status', models.CharField(blank=True, max_length=64, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('percent_share', models.FloatField(blank=True, null=True)),
                ('drilling_activity', models.CharField(blank=True, max_length=2000, null=True)),
                ('production_activity', models.CharField(blank=True, max_length=2183, null=True)),
                ('seismic_activity', models.CharField(blank=True, max_length=3254, null=True)),
                ('activity_type', models.CharField(blank=True, max_length=30, null=True)),
                ('point_size', models.CharField(blank=True, max_length=1, null=True)),
                ('day', models.CharField(blank=True, max_length=11, null=True)),
                ('project_code', models.CharField(blank=True, max_length=2000, null=True)),
            ],
            options={
                'db_table': 'INTERN_PRJ_PAW_ALL_ACTIVITY',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InternPrjPawDrillAct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('land_project', models.CharField(blank=True, max_length=64, null=True)),
                ('day', models.CharField(blank=True, max_length=10, null=True)),
                ('drilling_activity', models.CharField(blank=True, max_length=2000, null=True)),
            ],
            options={
                'db_table': 'INTERN_PRJ_PAW_DRILL_ACT',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='InternPrjPawSeisAct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('land_project', models.CharField(blank=True, max_length=64, null=True)),
                ('activity_date', models.DateField(blank=True, null=True)),
                ('seq', models.FloatField(blank=True, null=True)),
                ('col1', models.CharField(blank=True, max_length=2028, null=True)),
            ],
            options={
                'db_table': 'INTERN_PRJ_PAW_SEIS_ACT',
                'managed': False,
            },
        ),
    ]
