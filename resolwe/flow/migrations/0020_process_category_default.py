# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-12 08:21
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flow', '0019_relation_type_cicharfield'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='category',
            field=models.CharField(default='Other:', max_length=200, validators=[django.core.validators.RegexValidator(code='invalid_category', message='Category may be alphanumerics separated by colon', regex='^([a-zA-Z0-9]+[:\\-])*[a-zA-Z0-9]+:$')]),
        ),
    ]
