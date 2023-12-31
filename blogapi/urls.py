"""
URL configuration for blogapi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blogapp.views import Form, Blogs, BlogDetail, News, Comments
from django.conf.urls.static import static
from django.conf import settings
import os


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Form.as_view(), name= 'email'),
    path('blog/', Blogs.as_view(), name='blog'),
    path('blog/<int:pk>', BlogDetail.as_view(), name='blog'),
    path('news/', News.as_view(), name='news'),
    path('comment/', Comments.as_view(), name='comment'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)