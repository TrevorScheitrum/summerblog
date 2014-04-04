from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.fields.related import ManyToManyField

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length = 200)
    
    def __unicode__(self):
        return self.name
    
class Photo(models.Model):
    name = models.CharField(max_length = 200)
    photo = models.ImageField(upload_to="photos")
    
    def __unicode__(self):
        return self.name
    
class Article(models.Model):
    title = models.CharField(max_length = 200)
    date = models.DateTimeField()
    author = models.ForeignKey(Author)
    text = RichTextField(config_name='awesome_ckeditor')

    def __unicode__(self):
        return self.title