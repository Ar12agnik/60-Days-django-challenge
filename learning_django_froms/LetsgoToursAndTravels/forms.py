from django import forms
from .models import Tour
class TourForm(forms.Form):
    Tour=forms.ModelChoiceField(queryset=Tour.objects.all(),required=True,label='Tour')
    Name=forms.CharField(max_length=100,required=True,label='Name')
    phone=forms.IntegerField(required=True,label='Phone')
    address=forms.CharField(required=True,label='Address')
    insurance=forms.BooleanField(required=False,label='Travel Insurance')
    