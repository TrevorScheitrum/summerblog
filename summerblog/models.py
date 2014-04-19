from BeautifulSoup import BeautifulSoup
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.db.models.fields.related import ManyToManyField
from django.utils.html import format_html

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
    
class Article(models.Model):
    title = models.CharField(max_length = 200)
    date = models.DateTimeField()
    author = models.ForeignKey(User)
    text = RichTextField(config_name='awesome_ckeditor')

    @property
    def photos(self):
        soup = BeautifulSoup(self.text)
        _photos = soup.findAll('img')
        _photo_list = []
        
        for _photo in _photos:
            _photo_list.append([_photo['alt'], _photo['src']])
        return _photo_list
    
    def __unicode__(self):
        return self.title