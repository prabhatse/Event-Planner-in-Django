# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('user_reg', '0017_auto_20160128_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='phone_number',
            field=models.CharField(null=True, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,16}$')], max_length=16, blank=True, unique=True, verbose_name=b'Phone Number (e.g +254 712345678)'),
        ),
    ]
