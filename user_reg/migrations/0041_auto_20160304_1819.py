# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_reg', '0040_auto_20160226_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='category',
            field=models.CharField(max_length=3, verbose_name=b'Select categories below. ', choices=[(b'Bea', b'Beauty & Wellness'), (b'Mus', b'Music & Entertainment'), (b'Flo', b'Flowers & Decor'), (b'Cak', b'Cakes, Pastries & Desserts'), (b'Sta', b'Stationery & Branding'), (b'Fav', b'Gifts & Favours'), (b'Clo', b'Clothing & Accessories'), (b'Pho', b'Photography & Videography'), (b'Foo', b'Food & Drinks'), (b'Ven', b'Venue'), (b'Tra', b'Transport'), (b'Oth', b'Other')]),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='location',
            field=models.CharField(max_length=150, verbose_name=b'Where are you based?'),
        ),
    ]
