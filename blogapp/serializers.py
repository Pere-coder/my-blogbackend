from rest_framework import serializers
from .models import Form, Blog



class FormSerializer(serializers.ModelSerializer):
   class Meta:
       model = Form
       fields = ['email', 'date']
       

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['firstname', 'lastname', 'email', 'phone', 'blog']