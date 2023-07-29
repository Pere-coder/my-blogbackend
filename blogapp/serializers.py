from rest_framework import serializers
from .models import Form, Blog, News, Comment



class FormSerializer(serializers.ModelSerializer):
   class Meta:
       model = Form
       fields = ['email', 'date']
       

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'firstname', 'lastname', 'email', 'phone', 'blogtitle','image', 'blog', 'date']
        

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'image', 'News_title', 'News', ] 
        
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'comment']