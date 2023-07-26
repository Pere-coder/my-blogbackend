from django.contrib import admin
from .models import Form, Blog, News

class BlogAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'phone','blogtitle', 'blog', 'date')

class FormAdmin(admin.ModelAdmin):
    list_display = ("email", "date")

# Register your models here.
admin.site.register(Form, FormAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(News)

