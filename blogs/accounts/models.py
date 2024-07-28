from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class customUser(AbstractUser):
    phone_number=models.CharField(max_length=100 ,unique=True)
    user_bio=models.TextField(max_length=50)
    user_profile_image=models.ImageField(upload_to='profile_image',blank=True)
    USERNAME_FIELD='phone_number'
    REQUIRED_FIELDS=[]