from django import forms
from django.core import validators

#custom validation
def check_for_a(value):
	if value[0].lower() !='a':
		raise forms.ValidationError("Name needs to start with A")

class FormName(forms.Form):
	name = forms.CharField()
	#name = forms.CharField(validators=[check_for_a])
	email = forms.EmailField()
	verify_email= forms.EmailField(label="Enter your email address again")
	text = forms.CharField(widget=forms.Textarea)
	botcatcher = forms.CharField(required=False,
		                         widget=forms.HiddenInput,
		                         validators=[validators.MaxLengthValidator(0)])

	def clean(self):
		all_clean_data=super().clean()
		email=all_clean_data['email']
		vmail=all_clean_data['verify_email']

		if email!=vmail:
			raise forms.ValidationError("Make sure emails must match")

	"""def clean_botcatcher(self):
		botcatcher=self.cleaned_data['botcatcher']
		if len(botcatcher)>0:
			raise forms.ValidationError("buggy bot! surrender now XD ")
		return botcatcher """
