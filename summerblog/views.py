from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from summerblog.models import Article, Author, Photo, User
from photologue.models import Photo, Gallery
from photologue.managers import GalleryQuerySet, PhotoQuerySet

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
    
    paginator = Paginator(article_list, 5)

    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        articles = paginator.page(paginator.num_pages)
    
    
    for article in articles:
        article_backgrounds.append(article.background)

    context = {'articles' : articles, 'backgrounds' : article_backgrounds, 'article_archive' : article_archive}
    
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
    
def gallery(request):
    
    gallery_list = Gallery.objects.on_site().is_public().order_by('-date_added')
    
    context = {'gallery_list' : gallery_list}
    
    return render(request, 'summerblog/gallery_archive.html', context)

def photos(request, slug):

    gallery_list = Gallery.objects.on_site().is_public().get(slug=slug)
    
    context = {'object' : gallery_list}
    
    return render(request, 'summerblog/gallery_detail.html', context)
    