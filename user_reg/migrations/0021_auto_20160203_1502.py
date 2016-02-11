# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_reg', '0020_invitation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='message',
            field=models.TextField(max_length=500, verbose_name=b'Invitation Message'),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='subject',
            field=models.CharField(max_length=100, verbose_name=b'Invitation Subject'),
        ),
    ]
