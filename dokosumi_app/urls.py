"""stuply URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.search_rank, name='search_rank'),
    path('top/', views.top, name='top'),
    path('search_rank/', views.search_rank, name='search_rank'),
    path('result_rank/', views.result_rank, name='result_rank'),
    path('town_detail/<str:station_name>', views.town_detail, name='town_detail'),
    path('test/', views.test, name='test'),
]
