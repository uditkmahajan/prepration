"""boostup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from os import name
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",views.home,name="home"),
    path("test/",views.test,name="tests"),
    path("test/<str:slug>/",views.sub_test,name="sub_test"),
    path("download_paper/",views.download_paper,name="download"),
    path("download_paper/<str:slug>/",views.year,name="year"),
    path("download_paper/<str:slug1>/<str:slug2>/",views.paper,name="paper"),
    path("syllabus/",views.syllabus,name="syllabus"),
    path("syllabus/<str:slug>/",views.sub_syllabus,name="sub_syllabus"),
]
