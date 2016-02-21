# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_reg', '0027_budget_budgetitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitation',
            name='event',
        ),
        migrations.RemoveField(
            model_name='invitation',
            name='guest',
        ),
        migrations.RemoveField(
            model_name='invitation',
            name='guestlist',
        ),
        migrations.RemoveField(
            model_name='invitation',
            name='host',
        ),
        migrations.DeleteModel(
            name='Invitation',
        ),
    ]
