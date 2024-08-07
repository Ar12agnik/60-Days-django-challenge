from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('read_article/<int:blog_id>',views.read_article,name='read_article'),
    path('create',views.create_blog.as_view(),name='create_blog'),
    path('login',views.LoginView.as_view(),name='login'),
    path('logout',views.logout_view,name='logout'),
    path('accounts/',include('allauth.urls'))
]
