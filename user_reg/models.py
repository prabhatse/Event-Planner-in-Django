from django.db import models
from django.utils import timezone
from widgets import RemovableImageField
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import RegexValidator
from multiselectfield import MultiSelectField
from django.db.models import F, Sum

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
	date = models.DateField(blank=True, null=True)
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
	date = models.DateField(verbose_name="Date Due")
	time = models.TimeField(verbose_name="Time Due (e.g 14:30)")
	status = models.CharField(max_length=3, choices=task_status)

	def __unicode__(self):
    		return self.title

class Budget(models.Model):
	owner = models.ForeignKey('auth.User')
	event = models.ForeignKey(Event)
	title = models.CharField(max_length=70)
	description = models.TextField(max_length=100)

	def __unicode__(self):
    		return self.title

class BudgetItem(models.Model):
	owner = models.ForeignKey('auth.User')
	budget = models.ForeignKey(Budget)
	name = models.CharField(max_length=70, verbose_name="Name of Item")
	description = models.TextField(max_length=100)
	quantity = models.IntegerField(default=0, verbose_name="Number of Items")
	unit_cost = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Cost Per Item")
	
	def _get_total(self):
		return self.unit_cost * self.quantity
	total_cost = property(_get_total)

	def __unicode__(self):
    		return self.name

category_choices = (  
    ('Bea', 'Beauty & Wellness'),
    ('Mus', 'Music & Entertainment'),
    ('Flo', 'Flowers & Decor'),
    ('Cak', 'Cakes, Pastries & Desserts'),
    ('Sta', 'Stationery'),
    ('Fav', 'Gifts & Favours'),
    ('Clo', 'Clothing & Accessories'),
    ('Pho', 'Photography & Videography'),
    ('Foo', 'Food & Drinks'),
    ('Ven', 'Venue'),
    ('Tra', 'Transport'),
    ('Oth', 'Other'),
)


class Vendor(models.Model): 
	name = models.CharField(max_length=70, verbose_name="What's the name of your business? ")
	email = models.EmailField(max_length=70, unique=True, verbose_name="Email Address")
	phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+254712345678'. Up to 15 digits allowed. Please try again.")
	phone_number = models.CharField(max_length=15, validators=[phone_regex], unique=True, verbose_name="Phone Number (e.g +254712345678)")
	description = models.TextField(max_length=200, verbose_name="Tell us a bit about what makes your business unique. (Max characters: 200) ")
	location = models.CharField(max_length=70, verbose_name="Where are you based? (City, Country) ")
	category = models.CharField(max_length=3, choices=category_choices, verbose_name="Select categories below. ")
	website = models.URLField(blank=True)
	logo = RemovableImageField(blank=True, upload_to='vendors', verbose_name="Please upload your business logo or image. ")
	
	def __unicode__(self):
    		return self.name