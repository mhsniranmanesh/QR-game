# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-02-27 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Barcode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_id', models.IntegerField()),
                ('text', models.CharField(max_length=256)),
            ],
        ),
    ]
