# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user_reg', '0042_thereview'),
    ]

    operations = [
        migrations.AddField(
            model_name='thereview',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='thereview',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
