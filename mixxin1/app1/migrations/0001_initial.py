# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-19 07:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eno', models.CharField(max_length=50)),
                ('ename', models.CharField(max_length=50)),
                ('esal', models.FloatField()),
                ('eaddr', models.CharField(max_length=50)),
            ],
        ),
    ]
