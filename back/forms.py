from django import forms
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
from front import models
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class NewsForm(forms.ModelForm):

	class Meta:
		model = models.Post
		exclude = ["author"]
		widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required':"required"}), 
			'body': SummernoteWidget(attrs={'class': 'form-control', 'required':"required"}),
            'date': forms.TextInput(attrs={'class': 'form-control datepicker', 'required':"required"})
		}

class ObraForm(forms.ModelForm):
		
	class Meta:
		model = models.Obra
		exclude = ["author","tags"]
		widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required':"required"}), 
			'resume': SummernoteWidget(attrs={'class': 'form-control', 'required':"required"})
		}

class TagForm(forms.ModelForm):
		
	class Meta:
		model = models.TagObra
		fields = ["name"]
		widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required':"required"}), 
		}

class LinkObraForm(forms.ModelForm):
		
	class Meta:
		model = models.LinkObra
		exclude = ["obra"]
		widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required':"required"}), 
			'url': forms.TextInput(attrs={'class': 'form-control', 'required':"required"}), 
		}

class ChapterForm(forms.ModelForm):

	class Meta:
		model = models.Chapter
		exclude = ["obra"]
		widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required':"required"}), 
			'resume': SummernoteWidget(attrs={'class': 'form-control', 'required':"required"}),
		}

class ImageForm(forms.ModelForm):

	class Meta:
		model = models.Image
		exclude = ["author"]
		widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'required':"required"}), 
		}

class UserForm(forms.ModelForm):

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
		widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'required':"required"}), 
			'email': forms.EmailInput(attrs={'class': 'form-control', 'required':"required"}), 
		}

class AuthorForm(forms.ModelForm):
	
	class Meta:
		model = models.Author
		exclude = ["user"]
		widgets = {
			'bio': SummernoteWidget(attrs={'class': 'form-control', 'required':"required"}),
		}