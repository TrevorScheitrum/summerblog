from django.conf import settings
from django.conf.urls import patterns, url, include
from django.contrib import admin

from summerblog import views

admin.autodiscover()

urlpatterns = patterns('',     
    url(r'^$', 'summerblog.views.index', name='index'),
    url(r'^travelblog2014/$', 'summerblog.views.index', name='index'),
    url(r'^travelblog2014/gallery/$', 'summerblog.views.gallery', name='gallery'),
    url(r'^travelblog2014/gallery/(?P<slug>[\-\d\w]+)/$', 'summerblog.views.photos', name='photos'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^album', views.album, name='album'),
    (r'^photologue/', include('photologue.urls')),
    (r'^ckeditor/', include('ckeditor.urls')),
    (r'^progressbarupload/', include('progressbarupload.urls')),
    )
