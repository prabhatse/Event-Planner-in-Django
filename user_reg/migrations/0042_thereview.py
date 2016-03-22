# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_reg', '0041_auto_20160304_1819'),
    ]

    operations = [
        migrations.CreateModel(
            name='TheReview',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField(max_length=100)),
                ('rating', models.CharField(max_length=3, verbose_name=b'Please rate this vendor.', choices=[(b'Ter', b'Terrible'), (b'Poo', b'Poor'), (b'Ave', b'Average'), (b'Goo', b'Good'), (b'Exc', b'Excellent')])),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('vendor', models.ForeignKey(to='user_reg.Vendor')),
            ],
        ),
    ]
