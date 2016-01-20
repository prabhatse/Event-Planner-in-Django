# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_reg', '0009_auto_20160119_1436'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField(max_length=200)),
                ('venue', models.CharField(max_length=70, null=True, blank=True)),
                ('date', models.DateTimeField(null=True, blank=True)),
                ('category', models.CharField(max_length=3, choices=[(b'Bab', b'Baby Shower'), (b'Bir', b'Birthday Party'), (b'Cor', b'Corporate Event'), (b'Gra', b'Graduation Party'), (b'Wed', b'Wedding'), (b'Oth', b'Other')])),
                ('host', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
