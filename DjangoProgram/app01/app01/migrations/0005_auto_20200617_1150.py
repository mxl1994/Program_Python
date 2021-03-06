# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-17 03:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_auto_20200612_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=8)),
                ('dep', models.CharField(max_length=32)),
                ('province', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Emps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('age', models.IntegerField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=8)),
                ('province', models.CharField(max_length=32)),
                ('dep', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Dep')),
            ],
        ),
        migrations.RemoveField(
            model_name='authordetail',
            name='birthday',
        ),
    ]
