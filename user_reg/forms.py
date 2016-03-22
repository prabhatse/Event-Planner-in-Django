from django import forms
from django.contrib.auth.models import User
from user_reg.models import *
from django.conf import settings
from django.core.mail import send_mail
from django.template import loader
from django.template import RequestContext
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site
from django.forms.widgets import CheckboxSelectMultiple
import datetime

class MemberForm(forms.ModelForm):

	class Meta:
		model = Member
		fields = ('title', 'location', 'bio','website','image')


event_cat = ( 
    ('Bab', 'Baby Shower'),
    ('Bir', 'Birthday Party'),
    ('Cor', 'Corporate Event'),
    ('Gra', 'Graduation Party'),
    ('Wed', 'Wedding'),
    ('Oth', 'Other'),
)

class EventForm(forms.ModelForm):

    category = forms.ChoiceField(choices=event_cat)

    class Meta:
        model = Event
        widgets = {
            'date' : forms.DateInput(attrs={'class':'datepicker'})
        }
        fields = ('title','date','description','venue','category')

    def __init__(self, *args, **kwargs):
            super(EventForm, self).__init__(*args, **kwargs)
            self.fields['date'].widget.format = '%m/%d/%Y'

            def get_date(self):
                return self.modified.date()

    def clean_date(self):
            date = self.cleaned_data['date']
            if date:
                if date < datetime.date.today():
                    raise forms.ValidationError("The date cannot be in the past!")
                return date
            else:
                return date

class GuestlistForm(forms.ModelForm):

    class Meta:
        model = Guestlist
        fields = ('name', 'description')

class GuestForm(forms.ModelForm):

    class Meta:
        model = Guest
        fields = ('fname', 'lname', 'email', 'phone_number', 'guestlist')
    

class InvitationForm(forms.ModelForm):

    class Meta:
        model = Invitation
        fields = ('guestlist','guest','event','subject','message')

    def __init__(self, host, *args, **kwargs):
            super(InvitationForm, self).__init__(*args, **kwargs)
            self.fields['event'].queryset = Event.objects.filter(host=host)
            self.fields['guest'].queryset = Guest.objects.filter(host=host)
            self.fields['guestlist'].queryset = Guestlist.objects.filter(host=host)
	
task_status = (  
    ('Pen', 'Pending'),
    ('Pro', 'In Progress'),
    ('Com', 'Completed'),
    ('Ove', 'Overdue'),
) 

class TaskForm(forms.ModelForm):

    status = forms.ChoiceField(choices=task_status)

    class Meta:
        model = Task
        widgets = {
            'date' : forms.DateInput(attrs={'class':'datepicker'}),
        }
        fields = ('title','description','event','date','time','status')

    def __init__(self, host, *args, **kwargs):
            super(TaskForm, self).__init__(*args, **kwargs)
            self.fields['event'].queryset = Event.objects.filter(host=host)
            self.fields['date'].widget.format = '%m/%d/%Y'

            def get_date(self):
                return self.modified.date()

    def clean_date(self):
            date = self.cleaned_data['date']
            if date:
                if date < datetime.date.today():
                    raise forms.ValidationError("The date cannot be in the past!")
                return date
            else:
                return date

class BudgetForm(forms.ModelForm):

    class Meta:
        model = Budget
        fields = ('title','event','description')

    def __init__(self, host, *args, **kwargs):
            super(BudgetForm, self).__init__(*args, **kwargs)
            self.fields['event'].queryset = Event.objects.filter(host=host)

class BudgetItemForm(forms.ModelForm):

    class Meta:
        model = BudgetItem
        fields = ('budget','name','description','quantity','unit_cost')

    def __init__(self, owner, *args, **kwargs):
            super(BudgetItemForm, self).__init__(*args, **kwargs)
            self.fields['budget'].queryset = Budget.objects.filter(owner=owner)

category_choices = (  
    ('Bea', 'Beauty & Wellness'),
    ('Ent', 'Entertainment'),
    ('Dec', 'Flowers & Decor'),
    ('Cat', 'Catering & Cakes'),
    ('Sta', 'Stationery & Favours'),
    ('Clo', 'Clothing & Accessories'),
    ('Pho', 'Photography & Videography'),
    ('Jew', 'Jewellery'),
    ('Ven', 'Venues'),
    ('Tra', 'Transport'),
    ('Oth', 'Other'),
)

class VendorForm(forms.ModelForm):

    category = forms.CheckboxSelectMultiple(choices=category_choices)

    class Meta:
        model = Vendor
        fields = ('name','email','phone_number','description','location','category','website','logo')

rating_choices = (
    ('Ter', 'Terrible'),  
    ('Poo', 'Poor'),
    ('Ave', 'Average'),
    ('Goo', 'Good'),
    ('Exc', 'Excellent'),
)

class ReviewForm(forms.ModelForm):
    
    rating = forms.ChoiceField(choices=rating_choices)

    class Meta:
        model = TheReview
        fields = ('vendor', 'title','description','rating')

    def __init__(self, *args, **kwargs):
         super(ReviewForm, self).__init__(*args, **kwargs)