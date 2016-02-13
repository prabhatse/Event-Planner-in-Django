from django.db import models
from django.utils import timezone
from widgets import RemovableImageField
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import RegexValidator

event_cat = (  
    ('Bab', 'Baby Shower'),
    ('Bir', 'Birthday Party'),
    ('Cor', 'Corporate Event'),
    ('Gra', 'Graduation Party'),
    ('Wed', 'Wedding'),
    ('Oth', 'Other'),
) 

class Member(models.Model):
	user = models.OneToOneField(User)
	title = models.CharField(max_length=70, verbose_name="Job Title")
	location = models.CharField(max_length=70, verbose_name="Location")
	bio = models.TextField(max_length=200, verbose_name="About")
	website = models.URLField(blank=True)
	image = RemovableImageField(blank=True, null=True, upload_to='users', verbose_name="Profile Picture")
	
	# Override the __unicode__() method to return out something meaningful!
	def __unicode__(self):
    		return self.user.username

class Event(models.Model):
	host = models.ForeignKey('auth.User')
	title = models.CharField(max_length=70)
	description = models.TextField(max_length=200)
	venue = models.CharField(max_length=70, blank=True, null=True)
	date = models.DateField(blank=True, null=True, verbose_name="Date (DD/MM/YYYY)")
	category = models.CharField(max_length=3, choices=event_cat)

	def __unicode__(self):
    		return self.title

class Guestlist(models.Model):
	host = models.ForeignKey('auth.User')
	name = models.CharField(max_length=70)
	description = models.TextField(max_length=200)

	def __unicode__(self):
    		return self.name

class Guest(models.Model):
    host = models.ForeignKey('auth.User')
    guestlist = models.ForeignKey(Guestlist, blank=True, null=True)
    fname = models.CharField(max_length=70, verbose_name="First Name")
    lname = models.CharField(max_length=70, verbose_name="Last Name")
    email = models.EmailField(max_length=70, unique=True, verbose_name="Email Address")
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+254712345678'. Up to 15 digits allowed. Please try again.")
    phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=True, null=True, unique=True, verbose_name="Phone Number (e.g +254712345678)")

    def __unicode__(self):
    		return self.email

class Invitation(models.Model):
	host = models.ForeignKey('auth.User')
	guestlist = models.ForeignKey(Guestlist, blank=True, null=True)
	guest =  models.ForeignKey(Guest, blank=True, null=True)
	event = models.ForeignKey(Event)
	subject = models.CharField(max_length=100, verbose_name="Invitation Subject")
	message = models.TextField(max_length=500, verbose_name="Invitation Message")

task_status = (  
    ('Pen', 'Pending'),
    ('Pro', 'In Progress'),
    ('Com', 'Completed'),
    ('Ove', 'Overdue'),
) 

class Task(models.Model):
	host = models.ForeignKey('auth.User')
	title = models.CharField(max_length=70)
	description = models.TextField(max_length=200)
	event = models.ForeignKey(Event)
	due_date = models.DateField(verbose_name="Date Due (DD/MM/YYYY, eg 31/12/2016)")
	due_time = models.TimeField(verbose_name="Time Due (HH:MM 24 hour format, e.g 14:30")
	status = models.CharField(max_length=3, choices=task_status)

	def __unicode__(self):
    		return self.title
