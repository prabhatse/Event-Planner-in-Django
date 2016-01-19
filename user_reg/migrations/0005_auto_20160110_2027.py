# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user_reg', '0004_auto_20160110_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='bio',
            field=models.TextField(default=datetime.datetime(2016, 1, 10, 17, 26, 42, 961591, tzinfo=utc), max_length=200, verbose_name=b'About'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='member',
            name='title',
            field=models.CharField(default=datetime.datetime(2016, 1, 10, 17, 27, 27, 601823, tzinfo=utc), max_length=70, verbose_name=b'Job Title'),
            preserve_default=False,
        ),
    ]
