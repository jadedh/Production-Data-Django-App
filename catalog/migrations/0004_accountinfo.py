# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-05 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20170705_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=30)),
                ('type', models.CharField(max_length=10)),
                ('scope', models.CharField(blank=True, max_length=30, null=True)),
                ('description', models.CharField(blank=True, max_length=2000, null=True)),
                ('status', models.CharField(blank=True, max_length=30, null=True)),
                ('version', models.IntegerField(blank=True, null=True)),
                ('build', models.IntegerField(blank=True, null=True)),
                ('model_version', models.CharField(blank=True, max_length=64, null=True)),
                ('entitled', models.NullBooleanField()),
                ('audit_history', models.NullBooleanField()),
                ('audit_override', models.NullBooleanField()),
                ('auto_guid', models.NullBooleanField()),
                ('default_tablespace', models.CharField(blank=True, max_length=30, null=True)),
                ('temporary_tablespace', models.CharField(blank=True, max_length=30, null=True)),
                ('storage_configuration', models.CharField(blank=True, max_length=30, null=True)),
                ('security_configuration', models.CharField(blank=True, max_length=30, null=True)),
                ('coordinate_system', models.CharField(blank=True, max_length=64, null=True)),
                ('transform_wgs84', models.CharField(blank=True, max_length=64, null=True)),
                ('vertical_reference', models.CharField(blank=True, max_length=64, null=True)),
                ('unit_system', models.CharField(blank=True, max_length=30, null=True)),
                ('owner', models.CharField(max_length=30)),
                ('create_date', models.DateField(blank=True, null=True)),
                ('modify_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ACCOUNT_INFO',
                'managed': False,
            },
        ),
    ]
