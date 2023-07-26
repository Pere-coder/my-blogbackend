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
    date = models.DateTimeField(default=timezone.now)
    
    
    
class News(models.Model):
    image = models.ImageField()
    News = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    
    
# class YourModelName(models.Model):
#     # Other fields in your model
#     # ...

#     image_field = models.ImageField(upload_to='path/to/your/upload/directory/')
