from django.contrib import admin
from summerblog.models import Article, Author, Photo, ArticleHistory, Background
from photologue.models import Gallery

class ArticleInline(admin.StackedInline):
    model = Article
    extra = 3
    
class PhotoInline(admin.StackedInline):
    model = Photo
    extra = 3
    
class BackgroundAdmin(admin.ModelAdmin):
    model = Background
    fields = ('name', 'photo',)
    
class PhotoAdmin(admin.ModelAdmin):
    fields = ('name', 'photo',)

class ArticleHistoryAdmin(admin.ModelAdmin):
    fields = ('article','text',)

class ArticleHistoryInline(admin.StackedInline):
    fields = ('article','text',)
    
class ArticleAdmin(admin.ModelAdmin):
    fields = ('title', 'author','date','background','gallery', 'text', 'photos',) #'article_history',)
    readonly_fields = ('photos',)


myModels = [Article,ArticleAdmin]
#admin.site.register(myModels)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(ArticleHistory, ArticleHistoryAdmin)
admin.site.register(Background, BackgroundAdmin)