# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('user_reg', '0043_auto_20160322_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thereview',
            name='author',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
