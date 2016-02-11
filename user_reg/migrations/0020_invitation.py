# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_reg', '0019_auto_20160128_1527'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=500)),
                ('event', models.ForeignKey(to='user_reg.Event')),
                ('guest', models.ForeignKey(blank=True, to='user_reg.Guest', null=True)),
                ('guestlist', models.ForeignKey(blank=True, to='user_reg.Guestlist', null=True)),
                ('host', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
