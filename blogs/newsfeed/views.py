from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Blog,Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .forms import BlogForm,CommentForm

# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    return render(request,'blogs/index.html',{'blogs':blogs})
class create_blog(LoginRequiredMixin,View):
    def get(self,request):
        blog_form=BlogForm()
        return render(request,'blogs/create_blog.html',{'blog_form':blog_form})
    def post(self,request):
        blog_form=BlogForm(request.POST)
        if blog_form.isvalid():
            blog_form.save()
            return redirect('index')
        else:
            return render(request,'blogs/create_blog.html',{'blog_form':blog_form})
class comment_view(LoginRequiredMixin,View):
    def get(self,request,blog_id):
        blog=Blog.objects.get(id=blog_id)
        comment_form=CommentForm()
        return render(request,'blogs/comment.html',{'comment_form':comment_form,'blog':blog})
    def post(self,request,blog_id):
        blog=Blog.objects.get(id=blog_id)
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            comment=comment_form.save(commit=False)
            comment.blog=blog
            comment.save()
            return redirect('index')
        else:
            return render(request,'blogs/comment.html',{'comment_form':comment_form,'blog':blog})
        

