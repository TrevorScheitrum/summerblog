from BeautifulSoup import BeautifulSoup
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db.models.fields.related import ManyToManyField
from django.utils.html import format_html
from django_resized import ResizedImageField

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length = 200)

    def __unicode__(self):
        return self.name

class Photo(models.Model):
    name = models.CharField(max_length = 200)
    photo = models.CharField(max_length = 200)
    
    def __unicode__(self):
        return self.name
    
class Background(models.Model):
    name = models.CharField(max_length = 200)
    photo = ResizedImageField(max_width=1600, max_height=900, upload_to="backgrounds")
    
    def __unicode__(self):
        return self.name
    
class Article(models.Model):
    title = models.CharField(max_length = 200)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)
    background = models.ForeignKey(Background)
    text = RichTextField(config_name='awesome_ckeditor')

    @property
    def photos(self):
        soup = BeautifulSoup(self.text)
        _photos = soup.findAll('img')
        _photo_list = []
        
        for _photo in _photos:
            _photo_list.append([_photo['alt'], _photo['src']])
        return _photo_list
    

    
    def article_history(self):
        return ArticleHistory.objects.filter(article=self).order_by('-version')
    
    def save(self, *args, **kwargs):
        super(Article, self).save(*args, **kwargs)
        # save summary history
        article_history = self.article_history()
        if not article_history or self.text != article_history[0].text:
            newText = ArticleHistory(article=self, text=self.text)
            newText.save()
            
    def __unicode__(self):
        return self.title
    
    
class ArticleHistory(models.Model):
    version = models.IntegerField()
    article = models.ForeignKey(Article)
    text = models.TextField()
    
    #class Meta:
    #    unique_together = ('version', 'article',)
    
    def save(self, *args, **kwargs):
        # start with version 1 and increment it for each book
        current_version = ArticleHistory.objects.filter(article=self.article).order_by('-version')[:1]
        self.version = current_version[0].version + 1 if current_version else 1
        super(ArticleHistory, self).save(*args, **kwargs)
        
    def __unicode__(self):
        return self.article.title
