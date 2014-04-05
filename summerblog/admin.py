from django.contrib import admin
from summerblog.models import Article, Author, Photo2

class AuthorInline(admin.StackedInline):
    model = Author
    extra = 3

class ArticleInline(admin.StackedInline):
    model = Article
    extra = 3

class ArticleAdmin(admin.ModelAdmin):
    #inlines = [AuthorInline]
    fields = ('title', 'date', 'author', 'text', 'photos',)
    readonly_fields = ('photos',)


myModels = [Article,Author,Photo2]
#admin.site.register(myModels)
admin.site.register(Article, ArticleAdmin)
