from django import forms
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from front import models
from tinymce.models import HTMLField

class NewsForm(forms.ModelForm):
	body = HTMLField()
	def __init__(self,*args,**kwargs):
		self.request = kwargs.pop('request', None)
		super (NewsForm,self ).__init__(*args,**kwargs)
		self.fields['title'].widget=forms.TextInput(attrs={'class': 'form-control', 'required':"required"})
		self.fields['date'].widget=forms.TextInput(attrs={'class': 'form-control datepicker', 'required':"required"})

	class Meta:
		model = models.Post
		exclude = ["author"]

class ObraForm(forms.ModelForm):
	resume = HTMLField()
	def __init__(self,*args,**kwargs):
		self.request = kwargs.pop('request', None)
		super (ObraForm,self ).__init__(*args,**kwargs)
		self.fields['title'].widget = forms.TextInput(attrs={'class': 'form-control', 'required':"required"})

		
	class Meta:
		model = models.Obra
		exclude = ["author","tags"]

class TagForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		self.request = kwargs.pop('request', None)
		super (TagForm,self ).__init__(*args,**kwargs)
		self.fields['name'].widget = forms.TextInput(attrs={'class': 'form-control', 'required':"required"})
		
	class Meta:
		model = models.TagObra
		fields = ["name"]

class LinkObraForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		self.request = kwargs.pop('request', None)
		super (LinkObraForm,self ).__init__(*args,**kwargs)
		self.fields['title'].widget = forms.TextInput(attrs={'class': 'form-control', 'required':"required"})
		self.fields['url'].widget = forms.TextInput(attrs={'class': 'form-control', 'required':"required"})
		
	class Meta:
		model = models.LinkObra
		exclude = ["obra"]

class ChapterForm(forms.ModelForm):
	body = HTMLField()
	def __init__(self,*args,**kwargs):
		self.request = kwargs.pop('request', None)
		super (ChapterForm,self ).__init__(*args,**kwargs)
		self.fields['title'].widget = forms.TextInput(attrs={'class': 'form-control', 'required':"required"})

	class Meta:
		model = models.Chapter
		exclude = ["obra"]

class ImageForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		self.request = kwargs.pop('request', None)
		super (ImageForm,self ).__init__(*args,**kwargs)
		self.fields['title'].widget = forms.TextInput(attrs={'class': 'form-control', 'required':"required"})

	class Meta:
		model = models.Image
		exclude = ["author"]

class UserForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		self.request = kwargs.pop('request', None)
		super (UserForm,self ).__init__(*args,**kwargs)
		self.fields['username'].widget = forms.TextInput(attrs={'class': 'form-control', 'required':"required"})
		self.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control', 'required':"required"})

	class Meta:
		model = User
		include = ["username","email"]
		exclude = ["first_name",
		'last_name',
		'password',
		'groups',
		'user_permissions',
		'is_staff',
		'is_active',
		'is_superuser',
		'last_login',
		'date_joined']

class AuthorForm(forms.ModelForm):
	bio = HTMLField()
	def __init__(self,*args,**kwargs):
		self.request = kwargs.pop('request', None)
		super (AuthorForm,self ).__init__(*args,**kwargs)
	
	class Meta:
		model = models.Author
		exclude = ["user"]