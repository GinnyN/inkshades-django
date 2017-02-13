# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Publicity(models.Model):
	url= models.CharField(max_length=500,verbose_name="URL")
	image = models.ImageField(upload_to="publicidad/", verbose_name=u"Imagen")

class Afiliate(models.Model):
	url= models.CharField(max_length=500,verbose_name="URL")
	image = models.ImageField(upload_to="publicidad/", verbose_name=u"Imagen")

class Setting(models.Model):
	facebook = models.CharField(max_length=500,verbose_name=u"Facebook", blank=True)
	twitter = models.CharField(max_length=500,verbose_name=u"Twitter", blank=True)
	tumblr = models.CharField(max_length=500,verbose_name=u"Tumblr", blank=True)
	deviantart = models.CharField(max_length=500,verbose_name=u"DeviantArt", blank=True)
	subcultura = models.CharField(max_length=500,verbose_name=u"Subcultura", blank=True)
	facebookPageNumber = models.CharField(max_length=500,verbose_name=u"Facebook Page Number", blank=True)

class Author(models.Model):
	user = models.OneToOneField(User)
	avatar = models.ImageField(upload_to="avatar/",blank=True)
	bio = models.TextField()

	def __unicode__(self):
		return '%s' % self.user.username

class Post(models.Model):
	title = models.CharField(max_length=500,verbose_name=u"Título")
	date = models.DateTimeField(verbose_name=u"Fecha")
	author = models.ForeignKey(Author,verbose_name=u"Autor")
	body = models.TextField()
	spotlight = models.BooleanField(default=False, verbose_name=u"Destacado",blank=True)
	spotlight_image = models.ImageField(upload_to="spotlight/", verbose_name=u"Imagen para Destacar",blank=True)

	def __unicode__(self):
		return '%s' % self.title

class TagObra(models.Model):
	name = models.CharField(max_length=500,verbose_name=u"Nombre")

	def __unicode__(self):
		return '%s' % self.name

class Obra(models.Model):
	title = models.CharField(max_length=500,verbose_name=u"Título")
	author = models.ForeignKey(Author,verbose_name=u"Autor")
	resume = models.TextField(verbose_name=u"Resumen")
	obra_status = (
        ('Finalizada', u"Obra Finalizada"), 
        ('Continuada', u"Obra Continuada"),
        ('Unico', u"Capítulo Único"))
	status = models.CharField( max_length=20, choices=obra_status, default=obra_status[1][0], verbose_name=u"Status")
	tags = models.ManyToManyField(TagObra, null=True)
	cover = models.ImageField(upload_to="cover/", verbose_name=u"Portada", blank=True)

	def __unicode__(self):
		return '%s' % self.title

class Chapter(models.Model):
	title = models.CharField(max_length=500,verbose_name=u"Título")
	resume = models.TextField(verbose_name=u"Resumen")
	cover = models.ImageField(upload_to="cover/", verbose_name=u"Portada", blank=True)
	obra = models.ForeignKey(Obra)

	def __unicode__(self):
		return '%s' % self.title

class Page(models.Model):
	chapter = models.ForeignKey(Chapter)
	order = models.IntegerField(verbose_name="Orden")
	page = models.ImageField(upload_to="pages/", verbose_name=u"Páginas", blank=True)

	def __unicode__(self):
		return self.chapter.title + ": Page "+str(self.order)

class LinkObra(models.Model):
	title = models.CharField(max_length=500,verbose_name=u"Título")
	url= models.CharField(max_length=500,verbose_name="URL")
	obra = models.ForeignKey(Obra)

	def __unicode__(self):
		return '%s' % self.title

class LinkAuthor(models.Model):
	title = models.CharField(max_length=500,verbose_name=u"Título")
	url= models.CharField(max_length=500,verbose_name="URL")
	author = models.ForeignKey(Author)
	
	def __unicode__(self):
		return '%s' % self.title

class Image(models.Model):
	title= models.CharField(max_length=500,verbose_name=u"Título")
	author = models.ForeignKey(Author)
	cover = models.ImageField(upload_to="portfolio/", verbose_name=u"Imagen", blank=True)

	def __unicode__(self):
		return '%s' % self.title

class PtoVenta(models.Model):
	name = models.CharField(max_length=500,verbose_name=u"Nombre")
	address = models.CharField(max_length=500,verbose_name=u"Dirección")
	ciudad = models.CharField(max_length=500,verbose_name=u"Ciudad")
	image = models.ImageField(upload_to="ptoVenta/", verbose_name=u"Imagen")

	def __unicode__(self):
		return '%s' % self.name

class Productos(models.Model):
	body = models.TextField()

	def __unicode__(self):
		return "Productos"