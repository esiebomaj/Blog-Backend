"""blogbackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view


Blog_title = 'Blog API'
Blog_description = '''A simple web API for a blog 
with CRUD functionality, and user authenthication system (Token authenthication)'''
schema_view = get_swagger_view(title=Blog_title)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('post.urls')),
    path('api_auth/', include('rest_framework.urls')),
    path('api/v1/rest_auth/', include('rest_auth.urls')),
    path('api/v1/rest_auth/registration/',
         include('rest_auth.registration.urls')),
    path('docs/', include_docs_urls(title=Blog_title, description=Blog_description)),
    path('swagger_docs/', schema_view),

]
