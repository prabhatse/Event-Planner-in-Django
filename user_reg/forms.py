from django import forms
from django.contrib.auth.models import User
from user_reg.models import Member

class MemberForm(forms.ModelForm):

	class Meta:
		model = Member
		fields = ('title', 'location', 'bio','website','image')

	
