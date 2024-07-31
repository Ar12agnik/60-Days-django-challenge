from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('read_article/<int:blog_id>',views.read_article,name='read_article'),
]
