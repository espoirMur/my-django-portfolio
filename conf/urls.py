"""conf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.documentation import include_docs_urls

from .views import api_root

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('projects/', include('apps.projects.urls')),
    path('blog/', include('apps.blog.urls')),
    re_path('api/(?P<version>(v1|v2))/', include('apis.music.urls')),
    url(r'^docs/', include_docs_urls(title='Todo API',
                                     description='RESTful API for Todo')),
    url(r'^$', api_root),
    url(r'^', include(('apis.users.urls', 'users'), namespace='users')),
]
