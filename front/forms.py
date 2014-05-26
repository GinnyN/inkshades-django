from django import forms
from captcha.fields import CaptchaField

class ContactForm(forms.Form):
	name = forms.CharField(max_length=200, label="Nombre")
	email = forms.EmailField(label="E-mail")
	message = forms.CharField(label="Mensaje")
	captcha = CaptchaField(label="Human Test")

	def __init__(self,*args,**kwargs):
		self.request = kwargs.pop('request', None)
		super (ContactForm,self ).__init__(*args,**kwargs)
		self.fields['email'].widget = forms.TextInput(attrs={'class': 'form-control', 'required':"required"})
		self.fields['name'].widget = forms.TextInput(attrs={'class': 'form-control', 'required':"required"})
		self.fields['message'].widget = forms.Textarea(attrs={'class': 'form-control', 'required':"required"})