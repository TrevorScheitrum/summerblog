from django.contrib import admin
from summerblog.models import Article, Author, Photo2

class AuthorInline(admin.StackedInline):
    model = Author
    extra = 3
    
class ArticleInline(admin.StackedInline):
    model = Article
    extra = 3

class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleInline]


myModels = [Article,Author,Photo2]
admin.site.register(myModels)