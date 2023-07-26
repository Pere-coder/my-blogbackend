from django.shortcuts import render
from django.http import HttpResponseRedirect
from .serializers import FormSerializer, BlogSerializer, NewsSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from .models import Form, Blog, News
from django.db.models import Q


    
class Form(generics.ListCreateAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    
    

    
    
class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    
    
class Blogs(generics.ListCreateAPIView):
    serializer_class = BlogSerializer
    
    def get_queryset(self):
         queryset = Blog.objects.all()
         search_query = self.request.query_params.get('search', None)
         if search_query:
             queryset = queryset.filter(
                 Q(blogtitle__icontains=search_query)
                | Q(firstname__icontains=search_query)
                | Q(blog__icontains=search_query)
             )
         return queryset
     
    
class News(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer