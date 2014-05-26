from django.conf.urls import patterns, include, url
from front import views 

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'inkshades.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^post/(?P<post_id>\d+)$', views.Post.as_view(), name='post'),
    url(r'^$', views.Root.as_view(), name='root'),
    url(r'^page/(?P<page_nro>\d+)$', views.Page.as_view(), name='page'),
    url(r'^page/author/(?P<id>\d+)/(?P<page_nro>\d+)$', views.Page.as_view(), name='page-author'),
    url(r'^obras/$', views.Obras.as_view(), name='obras'),
    url(r'^obras/tag/(?P<tag>.+)$', views.Obras.as_view(), name='tags'),
    url(r'^obras/autor/(?P<id>\d+)$', views.Obras.as_view(), name='obra-autor'),
    url(r'^obra/(?P<id>\d+)$', views.Obra.as_view(), name='obra'),
    url(r'^autores/$', views.Autores.as_view(), name='autores'),
    url(r'^autor/(?P<id>\d+)$', views.Autor.as_view(), name='autor'),
    url(r'^venta/$', views.Venta.as_view(), name='venta'),
    url(r'^contacto/$', views.Contacto.as_view(), name='contacto'),
    url(r'^gracias/$', views.Gracias.as_view(), name='gracias'),
    url(r'^productos/$', views.Productos.as_view(), name='productos'),
)