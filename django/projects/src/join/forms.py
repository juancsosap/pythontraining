from django import forms
from .models import Join

class JoinForm(forms.ModelForm):
	class Meta:
		model = Join
		fields = ['full_name','email','zip_code']