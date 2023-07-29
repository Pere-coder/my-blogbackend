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
    blogtitle = models.CharField(max_length=100, default='Blog title')
    image = models.ImageField(default='myimage.jpg')
    blog = models.TextField(default='no blog post')
    date = models.DateField(auto_now_add=True)
    
    
    
class News(models.Model):
    image = models.ImageField()
    News_title = models.CharField(max_length=100, default='news title')
    News = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    
    
class Comment(models.Model):
    comment = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True)