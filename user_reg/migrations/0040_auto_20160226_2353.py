# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import user_reg.widgets


class Migration(migrations.Migration):

    dependencies = [
        ('user_reg', '0039_vendor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='logo',
            field=user_reg.widgets.RemovableImageField(upload_to=b'vendors', verbose_name=b'Please upload your business logo or image. ', blank=True),
        ),
    ]
