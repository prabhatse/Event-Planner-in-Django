from django import forms
from django.contrib.auth.models import User
from user_reg.models import *
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
            else
                return date
    



	
