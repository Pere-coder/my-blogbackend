from django.db import models
from django.utils import timezone






# Create your models here.

class Form(models.Model):
    email =  models.EmailField(max_length=100)
    date = models.DateField(auto_now_add=True)
    
    
class Blog(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    blog = models.TextField(default='no blog post')
    date = models.DateTimeField(default=timezone.now)