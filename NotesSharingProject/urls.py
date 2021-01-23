"""NotesSharingProject URL Configuration

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
from django.urls import path
from notes.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about',about,name='about'),
    path('contact',contact,name='contact'),
    path('login1',login1,name='login1'),
    path('admin1',admin1,name='admin1'),
    path('signup',signup,name='signup'),
    path('admin_home',admin_home,name='admin_home'),
    path('',index,name='index')
]
