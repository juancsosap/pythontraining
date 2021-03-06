# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-23 15:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('commune', models.CharField(max_length=100)),
                ('post_code', models.CharField(max_length=10)),
                ('street', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Condo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zone', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=100)),
                ('condo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='condo.Condo')),
            ],
        ),
    ]
