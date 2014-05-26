from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, FormView
from django.views.generic.edit import UpdateView
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from back import forms
from front import models

# Create your views here.

class Login(FormView):	
	template_name = 'auth.html'
	form_class = AuthenticationForm
	success_url = "/back/administrator/"

	def form_valid(self, form):
		login(self.request,form.get_user())
		return super(Login, self).form_valid(form)

class Administrator(TemplateView):
	template_name = "admin.html"

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(self.__class__, self).dispatch(request, *args, **kwargs)

class NewsList(TemplateView):
	template_name = "back/noticias.html"

	def get_context_data(self, **kwargs):
		context = super(NewsList, self).get_context_data(**kwargs)
		author = models.Author.objects.get(user=self.request.user)
		context["news"] = models.Post.objects.filter(author=author).order_by("date").reverse()
		return context

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(self.__class__, self).dispatch(request, *args, **kwargs)

class NewNews(FormView):
	template_name = "back/noticia.html"
	form_class = forms.NewsForm
	success_url = "/back/news/"

	def form_valid(self, form):
		author = models.Author.objects.get(user=self.request.user)
		models.Post(title=form.cleaned_data["title"],
			author=author,
			body=form.cleaned_data["body"],
			spotlight=form.cleaned_data["spotlight"],
			spotlight_image=form.cleaned_data["spotlight_image"],
			date=form.cleaned_data["date"]).save()
		return super(NewNews, self).form_valid(form)

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(self.__class__, self).dispatch(request, *args, **kwargs)

class NewsUpdate(View):

	def get(self, request, id):	
		form = forms.NewsForm(instance=models.Post.objects.get(pk=id))
		return render(request,"back/noticia-edit.html", {'form':form, "id":id})

	def post(self,request,id):
		form = forms.NewsForm(request.POST, request.FILES)
		if form.is_valid():
			news = models.Post.objects.get(id=id)
			news.title=form.cleaned_data["title"]
			news.body=form.cleaned_data["body"]
			news.spotlight=form.cleaned_data["spotlight"]
			news.spotlight_image=form.cleaned_data["spotlight_image"]
			news.date=form.cleaned_data["date"]
			news.save()
		return redirect("news-list")

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(self.__class__, self).dispatch(request, *args, **kwargs)

class NewsDelete(View):

	def get(self,request,id):
		models.Post.objects.get(id=id).delete()
		return redirect("news-list")

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(self.__class__, self).dispatch(request, *args, **kwargs)

class ObrasList(TemplateView):
	template_name = "back/obras.html"

	def get_context_data(self, **kwargs):
		context = super(ObrasList, self).get_context_data(**kwargs)
		author = models.Author.objects.get(user=self.request.user)
		context["obras"] = models.Obra.objects.filter(author=author)
		context["links"] = models.LinkObra.objects.filter(obra__in=context["obras"])
		return context

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(self.__class__, self).dispatch(request, *args, **kwargs)

class ObraNew(FormView):
	template_name = "back/nueva-obra.html"
	form_class = forms.ObraForm
	success_url = "/back/obras/"

	def form_valid(self, form):
		author = models.Author.objects.get(user=self.request.user)
		models.Obra(title=form.cleaned_data["title"],
			author=author,
			resume=form.cleaned_data["resume"],
			cover=form.cleaned_data["cover"],
			status=form.cleaned_data["status"]).save()
		return super(ObraNew, self).form_valid(form)

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(self.__class__, self).dispatch(request, *args, **kwargs)

class ObraUpdate(View):

	def get(self, request, id):	
		form = forms.ObraForm(instance=models.Obra.objects.get(pk=id))
		return render(request,"back/edit-obra.html", {'form':form, "id":id})

	def post(self,request,id):
		form = forms.ObraForm(request.POST, request.FILES)
		if form.is_valid():
			news = models.Obra.objects.get(id=id)
			news.title=form.cleaned_data["title"]
			news.resume=form.cleaned_data["resume"]
			news.status=form.cleaned_data["status"]
			if form.cleaned_data["cover"]:
				news.cover=form.cleaned_data["cover"]
			news.save()
		return redirect("list-obras")

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(self.__class__, self).dispatch(request, *args, **kwargs)

class ObraDelete(View):

	def get(self,request,id):
		models.Obra.objects.get(id=id).delete()
		return redirect("list-obras")

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(self.__class__, self).dispatch(request, *args, **kwargs) 

class ListTagsObra(View):

	def get(self,request,id):
		tags = models.TagObra.objects.all()
		obra = models.Obra.objects.get(pk=id)
		return render(request,"back/tag-obra.html", {'tags':tags, "obra":obra})

	def post(self,request,id):
		obra = models.Obra.objects.get(pk=id)
		obra.tags.clear()
		i = 1
		while i <= len(request.POST):
			try:
				if request.POST[str(i)] == "on":
					obra.tags.add(models.TagObra.objects.get(pk=i))
			except:
				pass
			i+=1
		return redirect("list-obras")

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(self.__class__, self).dispatch(request, *args, **kwargs)

class NewTags(FormView):
	template_name = "back/nueva-obra.html"
	form_class = forms.TagForm
	success_url = "/back/obras/"

	def form_valid(self, form):
		models.TagObra(name=form.cleaned_data["name"]).save()
		return super(NewTags, self).form_valid(form)

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(self.__class__, self).dispatch(request, *args, **kwargs)

class NewLinks(View):

	def get(self,request,id):
		form = forms.LinkObraForm()
		links = models.LinkObra.objects.filter(obra=models.Obra.objects.get(pk=id))
		return render(request,"back/links.html", {'form':form, "links":links})

	def post(self,request,id):
		try:
			models.LinkObra.objects.get(pk=request.POST["id"]).delete()
		except:
			form = forms.LinkObraForm(request.POST)
			if form.is_valid():
				models.LinkObra(title=form.cleaned_data["title"],
					url=form.cleaned_data["url"],
					obra=models.Obra.objects.get(pk=id)).save()
		return redirect(self.request.path)

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(self.__class__, self).dispatch(request, *args, **kwargs)

class ListChapter(TemplateView):
	template_name = "back/chapters.html"

	def get_context_data(self, **kwargs):
		context = super(ListChapter, self).get_context_data(**kwargs)
		author = models.Author.objects.get(user=self.request.user)
		context["chapters"] = models.Chapter.objects.filter(obra=models.Obra.objects.get(pk=kwargs["id"]))
		context["id"] = kwargs["id"]
		return context

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(self.__class__, self).dispatch(request, *args, **kwargs)

class DeleteChapter(View):

	def get(self, request, id, id_chapter):
		models.Chapter.objects.get(pk=id_chapter).delete()
		return redirect("chapter-obras", id=id)

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(self.__class__, self).dispatch(request, *args, **kwargs)

class EditChapter(View):

	def get(self, request, id, id_chapter):
		form = forms.ChapterForm(instance=models.Chapter.objects.get(pk=id_chapter))
		return render(request,"back/edit-chapter.html", {'form':form})

	def post(self, request, id, id_chapter):
		form = forms.ChapterForm(request.POST, request.FILES)
		if form.is_valid():
			news = models.Chapter.objects.get(id=id_chapter)
			news.title=form.cleaned_data["title"]
			news.resume=form.cleaned_data["resume"]
			if form.cleaned_data["cover"]:
				news.cover=form.cleaned_data["cover"]
			news.save()
		return redirect("chapter-obras", id=id)

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(self.__class__, self).dispatch(request, *args, **kwargs)

class NewChapter(View):

	def get(self, request, id):
		form = forms.ChapterForm()
		return render(request,"back/new-chapter.html", {'form':form})

	def post(self, request, id):
		form = forms.ChapterForm(request.POST, request.FILES)
		if form.is_valid():
			models.Chapter(title=form.cleaned_data["title"],
				resume=form.cleaned_data["resume"],
				cover=form.cleaned_data["cover"],
				obra=models.Obra.objects.get(pk=id)).save()
		return redirect("chapter-obras", id=id)

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(self.__class__, self).dispatch(request, *args, **kwargs)

class PortfolioList(TemplateView):
	template_name = "back/portfolio.html"

	def get_context_data(self, **kwargs):
		context = super(PortfolioList, self).get_context_data(**kwargs)
		author = models.Author.objects.get(user=self.request.user)
		context["image"] = models.Image.objects.filter(author=author)
		return context

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(self.__class__, self).dispatch(request, *args, **kwargs)

class NewImage(FormView):
	template_name = "back/nueva-image.html"
	form_class = forms.ImageForm
	success_url = "/back/portfolio/"

	def form_valid(self, form):
		models.Image(title=form.cleaned_data["title"],
			cover=form.cleaned_data["cover"],
			author=models.Author.objects.get(user=self.request.user)).save()
		return super(NewImage, self).form_valid(form)

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(self.__class__, self).dispatch(request, *args, **kwargs)

class DeleteImage(View):

	def get(self, request, id):
		models.Image.objects.get(pk=id).delete()
		return redirect("portfolio-list")

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(self.__class__, self).dispatch(request, *args, **kwargs)

class EditImage(View):

	def get(self, request, id):
		form = forms.ImageForm(instance=models.Image.objects.get(pk=id))
		return render(request,"back/edit-image.html", {'form':form})

	def post(self, request, id):
		form = forms.ImageForm(request.POST, request.FILES)
		if form.is_valid():
			image = models.Image.objects.get(pk=id)
			image.title = form.cleaned_data["title"]
			if form.cleaned_data["cover"]:
				image.cover = form.cleaned_data["cover"]
			image.save()
		return redirect("portfolio-list")

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(self.__class__, self).dispatch(request, *args, **kwargs)

class Perfil(TemplateView):
	template_name = "back/perfil.html"
	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(self.__class__, self).dispatch(request, *args, **kwargs)

class PerfilPassword(View):

	def get(self, request):
		form = PasswordChangeForm(user=request.user)
		return render(request,"back/password.html", {'form':form})

	def post(self, request):
		form = PasswordChangeForm(user=request.user, data=request.POST)
		if form.is_valid():
			form.save()
		return redirect("perfil")

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(self.__class__, self).dispatch(request, *args, **kwargs)

class PerfilInfo(View):

	def get(self, request):
		form = forms.UserForm(instance=request.user, prefix="user")
		form2 = forms.AuthorForm(instance=models.Author.objects.get(user=request.user),prefix="author")
		return render(request,"back/info.html", {'form':form, 'form2': form2})

	def post(self, request):
		form = forms.UserForm(data=request.POST, prefix="user")
		if form.is_valid():
			user = User.objects.get(pk=request.user.pk)
			user.username = form.cleaned_data["username"]
			user.email = form.cleaned_data["email"]
			user.save()
		form = forms.AuthorForm(data=request.POST, prefix="author")
		if form.is_valid():
			author = models.Author.objects.get(user=request.user)
			author.bio = form.cleaned_data["bio"]
			if form.cleaned_data["avatar"]:
				author.avatar = form.cleaned_data["avatar"]
			author.save()
		return redirect("perfil")

	@method_decorator(login_required)
	def dispatch(self, request, *args, **kwargs):
		return super(self.__class__, self).dispatch(request, *args, **kwargs)
