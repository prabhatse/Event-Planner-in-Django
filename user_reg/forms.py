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

    from_email = settings.DEFAULT_FROM_EMAIL

    recipient_list = [mail_tuple[1] for mail_tuple in settings.MANAGERS]

    subject_template_name = "invitation_subject.txt"

    template_name = 'invitation_form.txt'

    def __init__(self, data=None, files=None, request=None,
                 recipient_list=None, *args, **kwargs):
        if request is None:
            raise TypeError("Keyword argument 'request' must be supplied")
        self.request = request
        if recipient_list is not None:
            self.recipient_list = recipient_list
        super(InvitationForm, self).__init__(data=data, files=files,
                                          *args, **kwargs)

    def clean_invitee(self):
        guest = self.cleaned_data['guest']
        guestlist = self.cleaned_data['guestlist']
        if guest and guestlist == "":
            raise forms.ValidationError("You must select either a guest or a guestlist!")
        return date

    def message(self):
        """
        Render the body of the message to a string.

        """
        if callable(self.template_name):
            template_name = self.template_name()
        else:
            template_name = self.template_name
        return loader.render_to_string(template_name,
                                       self.get_context())

    def subject(self):
        """
        Render the subject of the message to a string.

        """
        subject = loader.render_to_string(self.subject_template_name,
                                          self.get_context())
        return ''.join(subject.splitlines())

    def get_context(self):
        """
        Return the context used to render the templates for the email
        subject and body.

        By default, this context includes:

        * All of the validated values in the form, as variables of the
          same names as their fields.

        * The current ``Site`` object, as the variable ``site``.

        * Any additional variables added by context processors (this
          will be a ``RequestContext``).

        """
        if not self.is_valid():
            raise ValueError(
                "Cannot generate Context from invalid contact form"
            )
        if Site._meta.installed:
            site = Site.objects.get_current()
        else:
            site = RequestSite(self.request)
        return RequestContext(self.request,
                              dict(self.cleaned_data,
                                   site=site))

    def get_message_dict(self):
        """
        Generate the various parts of the message and return them in a
        dictionary, suitable for passing directly as keyword arguments
        to ``django.core.mail.send_mail()``.

        By default, the following values are returned:

        * ``from_email``

        * ``message``

        * ``recipient_list``

        * ``subject``

        """
        if not self.is_valid():
            raise ValueError(
                "Message cannot be sent from invalid contact form"
            )
        message_dict = {}
        for message_part in ('from_email', 'message',
                             'recipient_list', 'subject'):
            attr = getattr(self, message_part)
            message_dict[message_part] = attr() if callable(attr) else attr
        return message_dict

    def save(self, fail_silently=False):
        """
        Build and send the email message.

        """
        send_mail(fail_silently=fail_silently, **self.get_message_dict())

	
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

    def __init__(self, owner, *args, **kwargs):
            super(BudgetForm, self).__init__(*args, **kwargs)
            self.fields['event'].queryset = Event.objects.filter(host=owner)

class BudgetItemForm(forms.ModelForm):

    class Meta:
        model = BudgetItem
        fields = ('budget','title', 'description', 'cost')

