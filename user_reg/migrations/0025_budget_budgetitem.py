# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_reg', '0024_auto_20160213_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField(max_length=100)),
                ('total_cost', models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)),
                ('event', models.ForeignKey(to='user_reg.Event')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BudgetItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=70, verbose_name=b'Name of Item')),
                ('description', models.TextField(max_length=100)),
                ('quantity', models.IntegerField(default=0, verbose_name=b'Number of Items')),
                ('unit_cost', models.DecimalField(verbose_name=b'Cost Per Item', max_digits=7, decimal_places=2)),
                ('total_cost', models.DecimalField(max_digits=7, decimal_places=2)),
                ('budget', models.ForeignKey(to='user_reg.Budget')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
