# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_reg', '0023_auto_20160210_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(verbose_name=b'Date Due (DD/MM/YYYY, eg 31/12/2016)'),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_time',
            field=models.TimeField(verbose_name=b'Time Due (HH:MM 24 hour format, e.g 14:30'),
        ),
    ]
