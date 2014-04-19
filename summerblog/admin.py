from django.contrib import admin
from summerblog.models import Article, Author, Photo

class AuthorInline(admin.StackedInline):
    model = Author
    extra = 3

class ArticleInline(admin.StackedInline):
    model = Article
    extra = 3
    
class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 3
    
class PhotoAdmin(admin.ModelAdmin):
    fields = ('name', 'photo',)

class ArticleAdmin(admin.ModelAdmin):
    fields = ('title', 'date', 'author', 'text', 'photos',)
    readonly_fields = ('photos',)


myModels = [Article,ArticleAdmin]
#admin.site.register(myModels)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Photo, PhotoAdmin)
