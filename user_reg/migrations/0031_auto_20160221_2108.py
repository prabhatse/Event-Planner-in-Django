# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_reg', '0030_auto_20160221_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budgetitem',
            name='total_cost',
            field=models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True),
        ),
    ]
