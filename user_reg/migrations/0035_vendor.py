# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import user_reg.widgets
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('user_reg', '0034_auto_20160225_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=70, verbose_name=b"What's the name of your business? ")),
                ('email', models.EmailField(unique=True, max_length=70, verbose_name=b'Email Address')),
                ('phone_number', models.CharField(unique=True, max_length=15, verbose_name=b'Phone Number (e.g +254712345678)', validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+254712345678'. Up to 15 digits allowed. Please try again.")])),
                ('description', models.TextField(max_length=200, verbose_name=b'Tell us a bit about what makes your business unique. (Max characters: 200) ')),
                ('location', models.CharField(max_length=70, verbose_name=b'Where are you based? (City, Country) ')),
                ('category', models.CharField(max_length=3, verbose_name=b'Select categories below. ', choices=[(b'Bea', b'Beauty & Wellness'), (b'Mus', b'Music & Entertainment'), (b'Flo', b'Flowers & Decor'), (b'Cak', b'Cakes, Pastries & Desserts'), (b'Sta', b'Stationery'), (b'Fav', b'Gifts & Favours'), (b'Clo', b'Clothing & Accessories'), (b'Pho', b'Photography & Videography'), (b'Foo', b'Food & Drinks'), (b'Ven', b'Venues'), (b'Tra', b'Transport'), (b'Oth', b'Other')])),
                ('website', models.URLField(blank=True)),
                ('logo', user_reg.widgets.RemovableImageField(upload_to=b'vendors', verbose_name=b'Please upload your business logo or image. ')),
            ],
        ),
    ]
