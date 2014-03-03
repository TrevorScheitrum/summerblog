from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from summerblog.models import Article, Author, Photo2

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django.utils import simplejson





def index(request):
    
    article_list = Article.objects.all().order_by('-date')
    
    context = {'articles' : article_list}
    
    return render(request, 'summerblog/index.html', context)
    