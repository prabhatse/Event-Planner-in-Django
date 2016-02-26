# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_reg', '0035_vendor'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Vendor',
        ),
    ]
