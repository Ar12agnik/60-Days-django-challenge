from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog,Comment

# Create your views here.
def index(request):
    blog=Blog.objects.all()
    return render(request,'blogs/index.html',{'blogs':blog})

