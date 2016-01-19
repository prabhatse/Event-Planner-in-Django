# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import user_reg.widgets


class Migration(migrations.Migration):

    dependencies = [
        ('user_reg', '0007_member_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='image',
            field=user_reg.widgets.RemovableImageField(upload_to=b'uploads/', verbose_name=b'Profile Picture', blank=True),
        ),
    ]
