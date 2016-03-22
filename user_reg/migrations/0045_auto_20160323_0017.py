# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_reg', '0044_auto_20160323_0016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='thereview',
            name='author',
        ),
        migrations.RemoveField(
            model_name='thereview',
            name='vendor',
        ),
        migrations.DeleteModel(
            name='TheReview',
        ),
    ]
