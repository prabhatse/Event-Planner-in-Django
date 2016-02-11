# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_reg', '0021_auto_20160203_1502'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField(max_length=200)),
                ('due_date', models.DateField(verbose_name=b'Date Due')),
                ('due_time', models.TimeField(verbose_name=b'Time Due')),
                ('status', models.CharField(max_length=3, choices=[(b'Pen', b'Pending'), (b'Pro', b'In Progress'), (b'Com', b'Completed'), (b'Ove', b'Overdue')])),
                ('event', models.ForeignKey(to='user_reg.Event')),
                ('host', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
