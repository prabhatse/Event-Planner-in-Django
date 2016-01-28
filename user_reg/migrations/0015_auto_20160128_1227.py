# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('user_reg', '0014_auto_20160128_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='phone_number',
            field=models.CharField(null=True, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+254711123456'. Up to 15 digits allowed.")], max_length=16, blank=True, unique=True, verbose_name=b'Phone Number (e.g +254 705 111 222'),
        ),
    ]
