# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-05 08:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0007_auto_20160303_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('is_capital', models.BooleanField()),
                ('area', models.BigIntegerField(blank=True, null=True)),
                ('population', models.BigIntegerField(blank=True, null=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.Country')),
            ],
            options={
                'verbose_name_plural': 'Cities (django-select2)',
            },
        ),
        migrations.AlterUniqueTogether(
            name='city',
            unique_together=set([('name', 'country')]),
        ),
    ]
