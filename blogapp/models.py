from django.db import models






# Create your models here.

class Form(models.Model):
    email =  models.EmailField(max_length=100)
    date = models.DateField(auto_now_add=True)
    
    
