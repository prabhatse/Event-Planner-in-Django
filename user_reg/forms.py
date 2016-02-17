from django import forms
from django.contrib.auth.models import User
from user_reg.models import *
from django.conf import settings
from django.core.mail import send_mail
from django.template import loader
from django.template import RequestContext
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site
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
        fields = ('title','date','description','venue','category')

	def __init__(self, *args, **kwargs):
            super(EventForm, self).__init__(*args, **kwargs)
            self.fields['date'].widget.format = '%d/%m/%Y'

            # at the same time, set the input format on the date field like you want it:
            self.fields['date'].input_formats = ['%d/%m/%Y']

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
        fields = ('title','description','event','due_date','due_time','status')

    def __init__(self, host, *args, **kwargs):
            super(TaskForm, self).__init__(*args, **kwargs)
            self.fields['event'].queryset = Event.objects.filter(host=host)
            self.fields['due_date'].widget.format = '%d/%m/%Y'

            # at the same time, set the input format on the date field like you want it:
            self.fields['due_date'].input_formats = ['%d/%m/%Y']

            def get_date(self):
                return self.modified.date()

    def clean_date(self):
            date = self.cleaned_data['due_date']
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
        fields = ('budget','title', 'description', 'cost')

