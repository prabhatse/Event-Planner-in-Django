# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('user_reg', '0028_auto_20160213_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='budget',
            name='total_cost',
            field=models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True),
        ),
    ]
