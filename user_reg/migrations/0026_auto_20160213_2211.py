# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_reg', '0025_budget_budgetitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budget',
            name='event',
        ),
        migrations.RemoveField(
            model_name='budget',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='budgetitem',
            name='budget',
        ),
        migrations.RemoveField(
            model_name='budgetitem',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Budget',
        ),
        migrations.DeleteModel(
            name='BudgetItem',
        ),
    ]
