# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import user_reg.widgets
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_reg', '0029_auto_20160221_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField(max_length=100)),
                ('total_cost', models.DecimalField(null=True, max_digits=7, decimal_places=2, blank=True)),
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
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField(max_length=200)),
                ('venue', models.CharField(max_length=70, null=True, blank=True)),
                ('date', models.DateField(null=True, verbose_name=b'Date (DD/MM/YYYY)', blank=True)),
                ('category', models.CharField(max_length=3, choices=[(b'Bab', b'Baby Shower'), (b'Bir', b'Birthday Party'), (b'Cor', b'Corporate Event'), (b'Gra', b'Graduation Party'), (b'Wed', b'Wedding'), (b'Oth', b'Other')])),
                ('host', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fname', models.CharField(max_length=70, verbose_name=b'First Name')),
                ('lname', models.CharField(max_length=70, verbose_name=b'Last Name')),
                ('email', models.EmailField(unique=True, max_length=70, verbose_name=b'Email Address')),
                ('phone_number', models.CharField(null=True, validators=[django.core.validators.RegexValidator(regex=b'^\\+?1?\\d{9,15}$', message=b"Phone number must be entered in the format: '+254712345678'. Up to 15 digits allowed. Please try again.")], max_length=15, blank=True, unique=True, verbose_name=b'Phone Number (e.g +254712345678)')),
            ],
        ),
        migrations.CreateModel(
            name='Guestlist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=70)),
                ('description', models.TextField(max_length=200)),
                ('host', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=100, verbose_name=b'Invitation Subject')),
                ('message', models.TextField(max_length=500, verbose_name=b'Invitation Message')),
                ('event', models.ForeignKey(to='user_reg.Event')),
                ('guest', models.ForeignKey(blank=True, to='user_reg.Guest', null=True)),
                ('guestlist', models.ForeignKey(blank=True, to='user_reg.Guestlist', null=True)),
                ('host', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=70, verbose_name=b'Job Title')),
                ('location', models.CharField(max_length=70, verbose_name=b'Location')),
                ('bio', models.TextField(max_length=200, verbose_name=b'About')),
                ('website', models.URLField(blank=True)),
                ('image', user_reg.widgets.RemovableImageField(upload_to=b'users', null=True, verbose_name=b'Profile Picture', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=70)),
                ('description', models.TextField(max_length=200)),
                ('due_date', models.DateField(verbose_name=b'Date Due (DD/MM/YYYY, eg 31/12/2016)')),
                ('due_time', models.TimeField(verbose_name=b'Time Due (HH:MM 24 hour format, e.g 14:30')),
                ('status', models.CharField(max_length=3, choices=[(b'Pen', b'Pending'), (b'Pro', b'In Progress'), (b'Com', b'Completed'), (b'Ove', b'Overdue')])),
                ('event', models.ForeignKey(to='user_reg.Event')),
                ('host', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='guest',
            name='guestlist',
            field=models.ForeignKey(blank=True, to='user_reg.Guestlist', null=True),
        ),
        migrations.AddField(
            model_name='guest',
            name='host',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='budget',
            name='event',
            field=models.ForeignKey(to='user_reg.Event'),
        ),
        migrations.AddField(
            model_name='budget',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
