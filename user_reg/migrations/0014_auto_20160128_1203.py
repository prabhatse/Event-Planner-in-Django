# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_reg', '0013_auto_20160127_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='guestlist',
            field=models.ForeignKey(blank=True, to='user_reg.Guestlist', null=True),
        ),
    ]
