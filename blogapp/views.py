from django.shortcuts import render
from django.http import HttpResponseRedirect
from .serializers import FormSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from .models import Form


    
class Form(generics.ListCreateAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer
    