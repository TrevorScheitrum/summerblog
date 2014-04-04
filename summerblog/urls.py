from django.conf.urls import patterns, url, include

from summerblog import views

urlpatterns = patterns('',
    #url(r'^', views.index, name='index'),
    url(r'^album', views.album, name='album'),
    (r'^ckeditor/', include('ckeditor.urls')),
    )
