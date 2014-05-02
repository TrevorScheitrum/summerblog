from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from summerblog.models import Article, Author, Photo, User

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
import json

from django.conf import settings
import boto




def index(request):
    
    article_list = Article.objects.all().order_by('-date')
    article_backgrounds = []
    
    article_archive = Article.objects.values('title', 'date', 'id').order_by("-date")
    
    for article in article_list:
        article_backgrounds.append(article.background)

    context = {'articles' : article_list, 'backgrounds' : article_backgrounds, 'article_archive' : article_archive}
    
    return render(request, 'summerblog/index.html', context)
    
def album(request):
    
    article_list = Article.objects.all().order_by('-date')
    photos = []
    
    for article in article_list:
        photos.append(article.photos)
    
    
    context = {'photos' : photos}
    
    return render(request, 'summerblog/album.html', context)
    
    context = {'photos' : photo_list}
    
    return render(request, 'summerblog/album.html', context)
    