from django.conf.urls import url, include
from back import views 
from django.contrib.auth.decorators import login_required


urlpatterns = [
    # Examples:
    # url(r'^$', 'inkshades.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^obras/tag/(?P<tag>.+)$', views.Obras.as_view(), name='tags'),    
    #url(r'^autor/(?P<id>\d+)$', views.Autor.as_view(), name='autor'),
    url(r'^$', views.Login.as_view(), name='login'),
    url(r'^administrator/$', views.Administrator.as_view(), name='administrator'),
    url(r'^news/$', views.NewsList.as_view(), name='news-list'),
    url(r'^new/$', views.NewNews.as_view(), name='new-news'),
    url(r'^new/(?P<id>\d+)$', views.NewsUpdate.as_view(), name='update-news'),
    url(r'^new/delete/(?P<id>\d+)$', views.NewsDelete.as_view(), name='delete-news'),
    url(r'^obras/$', views.ObrasList.as_view(), name='list-obras'),
    url(r'^obras/new/$', views.ObraNew.as_view(), name='new-obras'),
    url(r'^obras/update/(?P<id>\d+)$', views.ObraUpdate.as_view(), name='update-obras'),
    url(r'^obras/delete/(?P<id>\d+)$', views.ObraDelete.as_view(), name='delete-obras'),
    url(r'^obras/tags/(?P<id>\d+)$', views.ListTagsObra.as_view(), name='tag-obras'),
    url(r'^obras/tags/new/$', views.NewTags.as_view(), name='new-tag'),
    url(r'^obras/link/(?P<id>\d+)$', views.NewLinks.as_view(), name='link-obras'),
    url(r'^obras/chapter/(?P<id>\d+)$', views.ListChapter.as_view(), name='chapter-obras'),
    url(r'^obras/chapter/delete/(?P<id>\d+)/(?P<id_chapter>\d+)$', views.DeleteChapter.as_view(), name='chapter-delete'),
    url(r'^obras/chapter/edit/(?P<id>\d+)/(?P<id_chapter>\d+)$', views.EditChapter.as_view(), name='chapter-edit'),
    url(r'^obras/chapter/new/(?P<id>\d+)$', views.NewChapter.as_view(), name='chapter-new'),
    url(r'^portfolio/$', views.PortfolioList.as_view(), name='portfolio-list'),
    url(r'^portfolio/new/$', views.NewImage.as_view(), name='portfolio-new'),
    url(r'^portfolio/delete/(?P<id>\d+)$', views.DeleteImage.as_view(), name='portfolio-delete'),
    url(r'^portfolio/edit/(?P<id>\d+)$', views.EditImage.as_view(), name='portfolio-edit'),
    url(r'^perfil/$', views.Perfil.as_view(), name='perfil'),
    url(r'^perfil/password/$', views.PerfilPassword.as_view(), name='perfil-password'),
    url(r'^perfil/info/$', views.PerfilInfo.as_view(), name='perfil-info'),
    #url(r'^noticias/$', views.Administrator.as_view(), name='administrator'),
    url(r'^logout/$', views.logout_view, name="logout"),
]