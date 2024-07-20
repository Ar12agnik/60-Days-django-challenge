from django import forms
from .models import Tour,agencies,places
class TourForm(forms.Form):
    Tour=forms.ModelChoiceField(queryset=Tour.objects.all(),required=True,label='Tour',widget=forms.RadioSelect)
    Name=forms.CharField(max_length=100,required=True,label='Name')
    phone=forms.IntegerField(required=True,label='Phone')
    address=forms.CharField(required=True,label='Address')
    insurance=forms.BooleanField(required=False,label='Travel Insurance')
class addTourForm(forms.ModelForm):
    class Meta:
        model=Tour
        fields='__all__'
    insurance=forms.BooleanField(required=False,label='Travel Insurance')
class addAgenciesForm(forms.ModelForm):
    class Meta:
        model=agencies
        fields='__all__'
    insurance=forms.BooleanField(required=False,label='Travel Insurance')
class addPlacesForm(forms.ModelForm):
    class Meta:
        model=places
        fields='__all__'
