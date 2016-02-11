# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user_reg', '0022_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due_time',
            field=models.TimeField(default=datetime.datetime(2016, 2, 10, 10, 48, 17, 731597, tzinfo=utc), verbose_name=b'Time Due'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(verbose_name=b'Date Due'),
        ),
    ]
