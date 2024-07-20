from django import forms
from .models import Tour,agencies,places,pictures
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
class TourForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(TourForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name!='insurance':
                visible.field.widget.attrs['class'] = 'form-control'
            
    Tour=forms.ModelChoiceField(queryset=Tour.objects.all(),required=True,label='Tour')
    Name=forms.CharField(max_length=100,required=True,label='Name')
    phone=forms.IntegerField(required=True,label='Phone')
    address=forms.CharField(required=True,label='Address')
    insurance=forms.BooleanField(required=False,label='Travel Insurance',widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
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

class pictures_upload_form(forms.ModelForm):
    class Meta:
        model=pictures
        fields='__all__'
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
    def __init__(self, *args, **kwargs):
        super(pictures_upload_form, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_method = 'post'
        self.helper.form_enctype = 'multipart/form-data'
        self.helper.add_input(Submit('submit', 'Submit'))