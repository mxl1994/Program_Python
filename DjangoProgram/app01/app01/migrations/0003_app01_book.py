# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-12 02:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20200612_1035'),
    ]

    operations = [
        migrations.CreateModel(
            name='app01_book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('publish', models.CharField(max_length=32)),
                ('pub_date', models.DateField()),
            ],
        ),
    ]
