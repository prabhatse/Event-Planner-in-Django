# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_reg', '0031_auto_20160221_2108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budget',
            name='total_cost',
        ),
        migrations.RemoveField(
            model_name='budgetitem',
            name='total_cost',
        ),
    ]
