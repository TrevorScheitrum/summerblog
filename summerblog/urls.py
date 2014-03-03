from django.conf.urls import patterns, url, include

from summerblog import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    (r'^ckeditor/', include('ckeditor.urls')),
    )
