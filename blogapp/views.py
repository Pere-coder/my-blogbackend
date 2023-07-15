from django.shortcuts import render
from django.http import HttpResponseRedirect
from .serializers import FormSerializer, BlogSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from .models import Form, Blog


    
class Form(generics.ListCreateAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    
    
class Blog(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer