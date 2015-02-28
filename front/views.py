# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import View, TemplateView, FormView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from front import models, forms
from django.core.mail import send_mail
# Create your views here.

class Post(TemplateView):

	template_name = "post.html"

	def get_context_data(self, **kwargs):
		context = super(Post, self).get_context_data(**kwargs)
		context["post"] = models.Post.objects.get(pk=kwargs["post_id"])
		return context

class Root(TemplateView):

	template_name = "root.html"

	def get_context_data(self, **kwargs):
		context = super(Root, self).get_context_data(**kwargs)
		context["posts"] = models.Post.objects.order_by('date').reverse()[:5]
		context["spotlight"] = models.Post.objects.order_by('date').filter(spotlight=True).reverse()[:5]
		return context

class Page(TemplateView):

	template_name = "pagination.html"

	def get_context_data(self, **kwargs):
		context = super(Page, self).get_context_data(**kwargs)
		try:
			data = models.Post.objects.filter(author__pk=kwargs["id"]).order_by('date').reverse()
			context["author"] = models.Author.objects.get(pk=kwargs["id"])
			context["authorLink"] = kwargs["id"]
		except:
			data = models.Post.objects.order_by('date').reverse()
		
		pages = Paginator(data,10)
		try:
			context["posts"] = pages.page(kwargs["page_nro"])
		except PageNotAnInteger:
        # If page is not an integer, deliver first page.
			context["posts"] = pages.page(1)
		except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
			context["posts"] = pages.page(pages.num_pages)
		context["number_pages"] = pages.page_range
		context["pages_number"] = kwargs["page_nro"]
		context["next"] = context["posts"].has_next()
		context["page_next"] = int(kwargs["page_nro"]) + 1
		context["previous"] = context["posts"].has_previous()
		context["page_previous"] = int(kwargs["page_nro"]) - 1
		return context

class Obras(TemplateView):

	template_name = "obras.html"

	def get_context_data(self, **kwargs):
		context = super(Obras, self).get_context_data(**kwargs)
		try:
			context["tag"] = kwargs["tag"]
			context["obras"] = models.Obra.objects.filter(tags__name=kwargs["tag"]).order_by("title")
		except: 
			try:
				context["autor"] = models.Author.objects.get(pk=kwargs["id"])
				context["obras"] = models.Obra.objects.filter(author=context["autor"]).order_by("title")
			except:
				context["obras"] = models.Obra.objects.order_by("title")

		context["links"] = models.LinkObra.objects.filter(obra__in=context["obras"])

		return context

class Obra(TemplateView):

	template_name = "obra.html"

	def get_context_data(self, **kwargs):
		context = super(Obra, self).get_context_data(**kwargs)
		context["obra"] = models.Obra.objects.get(pk=kwargs["id"])
		context["chapters"] = models.Chapter.objects.filter(obra=context["obra"])
		context["links"] = models.LinkObra.objects.filter(obra=context["obra"])
		return context

class Autores(TemplateView):

	template_name = "autores.html"

	def get_context_data(self, **kwargs):
		context = super(Autores, self).get_context_data(**kwargs)
		context["autores"] = models.Author.objects.order_by("username")
		context["links"] = models.LinkAuthor.objects.all()
		return context

class Autor(TemplateView):

	template_name = "autor.html"

	def get_context_data(self, **kwargs):
		context = super(Autor, self).get_context_data(**kwargs)
		context["autor"] = models.Author.objects.get(pk=kwargs["id"])
		context["links"] = models.LinkAuthor.objects.filter(author=context["autor"])
		context["obras"] = models.Obra.objects.filter(author=context["autor"])
		context["noticias"] = models.Post.objects.filter(author=context["autor"]).order_by("date").reverse()
		context["images"] = models.Image.objects.filter(author=context["autor"])
		return context

class Venta(TemplateView):
	template_name = "venta.html"

	def get_context_data(self, **kwargs):
		context = super(Venta, self).get_context_data(**kwargs)
		context["venta"] = models.PtoVenta.objects.all().order_by("ciudad","name")
		return context

class Gracias(TemplateView):
	template_name = "gracias.html"

class Contacto(FormView):	
	template_name = 'contact.html'
	form_class = forms.ContactForm
	success_url = "/gracias/"

	def form_valid(self, form):
		send_mail("Contacto Ink Shades", form.cleaned_data["name"]+": "+form.cleaned_data["message"], form.cleaned_data["email"], ["satelliteg@gmail.com"], fail_silently=False)
		return super(Contacto, self).form_valid(form)

class Productos(TemplateView):
	template_name="productos.html"

	def get_context_data(self, **kwargs):
		context = super(Productos, self).get_context_data(**kwargs)
		context["productos"] = models.Productos.objects.get(pk=1)
		return context	
    