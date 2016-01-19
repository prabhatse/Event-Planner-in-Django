# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user_reg', '0006_auto_20160119_1203'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='location',
            field=models.CharField(default=datetime.datetime(2016, 1, 19, 9, 41, 10, 478722, tzinfo=utc), max_length=70, verbose_name=b'Location'),
            preserve_default=False,
        ),
    ]
