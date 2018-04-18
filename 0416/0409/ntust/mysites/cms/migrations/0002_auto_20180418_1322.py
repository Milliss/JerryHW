# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-18 05:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Namess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namee', models.CharField(max_length=87)),
                ('nickname', models.CharField(max_length=87)),
                ('birthdayy', models.DecimalField(decimal_places=0, max_digits=7)),
                ('constellation', models.CharField(max_length=87)),
            ],
        ),
        migrations.AlterField(
            model_name='food',
            name='comment',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
