from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Blog,Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from .forms import BlogForm,CommentForm
from django.contrib.auth import logout
from accounts.forms import update_user

# Create your views here.
def index(request):
    auth = request.user.is_authenticated
    user = request.user if auth else None
    if request.method=='GET':
        if user:
            print(type(user.user_bio))
            if user.user_bio is None or user.user_bio=='':
                form=update_user()
                return render(request,'accounts/update_user.html',{'form':form})
    if request.method=='POST':
        print("post")
        form=update_user(request.POST,request.FILES,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request,'accounts/update_user.html',{'form':form})
    
    blogs = Blog.objects.all().order_by('-id', 'likes')
    
    context = {
        'blogs': blogs,
        'user': user,
        'auth': auth
    }
    
    return render(request, 'blogs/index.html', context)
class create_blog(LoginRequiredMixin,View):
    def get(self,request):
        blog_form=BlogForm()
        return render(request,'blogs/create_blog.html',{'blog_form':blog_form})
    def post(self,request):
        blog_form=BlogForm(request.POST,request.FILES)
        if blog_form.is_valid():
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
def read_article(request,blog_id):
    auth = request.user.is_authenticated
    user = request.user if auth else None
    
    try:
        blog=Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        return redirect('index')
    comment=Comment.objects.filter(post=blog).order_by('-created_at')
    if request.method=='POST':
        comment_form=CommentForm(request.POST)
        if comment_form.is_valid():
            print("valid")
            comment=comment_form.save()
            comment.post=blog
            comment.save()
            return redirect('read_article',blog_id)
        else:
            return render(request,'blogs/read_article.html',{'blog':blog,'comments':comment,'comment_form':comment_form,'auth':auth})
    else:
        comment_form=CommentForm(initial={'post':blog,'user':request.user})
        return render(request,'blogs/read_article.html',{'blog':blog,'comments':comment,'comment_form':comment_form,'auth':auth})
class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            return render(request, 'blogs/login.html')
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('index')