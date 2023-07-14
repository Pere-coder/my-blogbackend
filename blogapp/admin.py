from django.contrib import admin
from .models import Form

class FormAdmin(admin.ModelAdmin):
    list_display = ("email", "date")

# Register your models here.
admin.site.register(Form, FormAdmin)

