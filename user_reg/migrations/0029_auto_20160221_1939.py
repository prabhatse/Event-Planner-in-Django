# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_reg', '0028_auto_20160221_1919'),
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
        migrations.RemoveField(
            model_name='event',
            name='host',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='guestlist',
        ),
        migrations.RemoveField(
            model_name='guest',
            name='host',
        ),
        migrations.RemoveField(
            model_name='guestlist',
            name='host',
        ),
        migrations.RemoveField(
            model_name='member',
            name='user',
        ),
        migrations.RemoveField(
            model_name='task',
            name='event',
        ),
        migrations.RemoveField(
            model_name='task',
            name='host',
        ),
        migrations.DeleteModel(
            name='Budget',
        ),
        migrations.DeleteModel(
            name='BudgetItem',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
        migrations.DeleteModel(
            name='Guest',
        ),
        migrations.DeleteModel(
            name='Guestlist',
        ),
        migrations.DeleteModel(
            name='Member',
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
