#import django_summernote
import front
import captcha
from django.conf import settings

from django.conf.urls import url, include

from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'inkshades.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', admin.site.urls),
    #url(r'^summernote/', django_summernote.urls),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^',include('front.urls')),
    url(r'^back/',include('back.urls')),
    url(r'^captcha/', include('captcha.urls')),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += [
        (r'^media/(?P<path>.*)$', include('django.views.static.serve'), {
        'document_root': settings.MEDIA_ROOT}),
        (r'^static/(?P<path>.*)$', include('django.views.static.serve'), {
        'document_root': settings.STATIC_ROOT})
    ]