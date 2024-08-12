from django.shortcuts import render
from django.contrib.auth import get_user_model
from newsfeed.models import Blog
# Create your views here.
def profile(request):
    loggin= request.user.is_authenticated
    user=request.user
    blogs=Blog.objects.filter(user=user)
    return render(request, 'accounts/profile.html',{'user':user,'blogs':blogs,'loggin':loggin})

def view_profile(request,username):
    loggin= request.user.is_authenticated
    User = get_user_model()
    user=User.objects.get(username=username)
    blogs=Blog.objects.filter(user=user)
    return render(request, 'accounts/profile.html',{'user':user,'blogs':blogs,'loggin':loggin})