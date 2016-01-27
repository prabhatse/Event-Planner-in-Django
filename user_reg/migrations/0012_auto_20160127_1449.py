# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('user_reg', '0011_auto_20160119_1959'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(max_length=70, verbose_name=b'First Name')),
                ('lname', models.CharField(max_length=70, verbose_name=b'Last Name')),
                ('email', models.EmailField(unique=True, max_length=70, verbose_name=b'Email Address')),
                ('phone_number', models.CharField(blank=True, max_length=15, unique=True, null=True, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+254711123456'. Up to 15 digits allowed.")])),
            ],
        ),
        migrations.CreateModel(
            name='Guestlist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=70)),
                ('description', models.TextField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='guest',
            name='guestlist',
            field=models.ForeignKey(to='user_reg.Guestlist'),
        ),
    ]
