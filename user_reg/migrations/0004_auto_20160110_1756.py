# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import user_reg.widgets


class Migration(migrations.Migration):

    dependencies = [
        ('user_reg', '0003_member'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='member',
            name='lname',
        ),
        migrations.AlterField(
            model_name='member',
            name='bio',
            field=models.TextField(max_length=200, null=True, verbose_name=b'About', blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='image',
            field=user_reg.widgets.RemovableImageField(upload_to=b'static/back-end/img/users', null=True, verbose_name=b'Profile Picture', blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='title',
            field=models.CharField(max_length=70, null=True, verbose_name=b'Job Title', blank=True),
        ),
    ]
