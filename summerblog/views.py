from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from summerblog.models import Article, Author, Photo, User

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.utils import simplejson

from django.conf import settings
import boto




def index(request):
    
    article_list = Article.objects.all().order_by('-date')
    
    user_articles = []

    context = {'articles' : article_list, 'user_articles': user_articles}
    
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
    