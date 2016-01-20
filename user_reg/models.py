from django.db import models
from django.utils import timezone
from widgets import RemovableImageField
from django.contrib.auth.models import User
from django.conf import settings

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
