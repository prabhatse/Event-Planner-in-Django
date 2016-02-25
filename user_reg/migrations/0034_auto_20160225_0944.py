# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_reg', '0033_auto_20160224_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='time',
            field=models.TimeField(verbose_name=b'Time Due (e.g 14:30)'),
        ),
    ]
