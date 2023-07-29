from django.contrib import admin
from .models import Form, Blog, News, Comment

class BlogAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'phone','blogtitle','image', 'blog', 'date')

class FormAdmin(admin.ModelAdmin):
    list_display = ("email", "date")
    
class NewsAdmin(admin.ModelAdmin):
    list_display = ("News_title", "image", "News")
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "comment")

# Register your models here.
admin.site.register(Form, FormAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Comment, CommentAdmin)

