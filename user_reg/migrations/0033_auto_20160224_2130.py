# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user_reg', '0032_auto_20160222_1220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='due_date',
        ),
        migrations.RemoveField(
            model_name='task',
            name='due_time',
        ),
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 2, 24, 18, 30, 10, 314449, tzinfo=utc), verbose_name=b'Date Due'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='time',
            field=models.TimeField(default=datetime.datetime(2016, 2, 24, 18, 30, 20, 302460, tzinfo=utc), verbose_name=b'Time Due'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(null=True, blank=True),
        ),
    ]
