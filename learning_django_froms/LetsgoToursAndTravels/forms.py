from django import forms
from .models import Tour,agencies,places,pictures,bookings
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
# class TourForm(forms.Form):
#     def __init__(self, *args, **kwargs):
#         super(TourForm, self).__init__(*args, **kwargs)
#         for visible in self.visible_fields():
#             if visible.name!='insurance':
#                 visible.field.widget.attrs['class'] = 'form-control'
#         self.helper = FormHelper(self)
#         self.helper.add_input(Submit('submit', 'Submit'))
            
#     Tour=forms.ModelChoiceField(queryset=Tour.objects.all(),required=True,label='Tour')
#     Name=forms.CharField(max_length=100,required=True,label='Name')
#     phone=forms.IntegerField(required=True,label='Phone')
#     address=forms.CharField(required=True,label='Address')
#     insurance=forms.BooleanField(required=False,label='Travel Insurance',widget=forms.CheckboxInput(attrs={'class':'form-check-input'}))
from django import forms
from .models import bookings
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class TourForm(forms.ModelForm):
    class Meta:
        model = bookings
        fields = '__all__'
        widgets = {
            'User': forms.HiddenInput()
        }

    def __init__(self, *args, **kwargs):
        super(TourForm, self).__init__(*args, **kwargs) 
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))

class addTourForm(forms.ModelForm):
    insurance = forms.BooleanField(required=False, label='Travel Insurance')

    class Meta:
        model = Tour
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(addTourForm, self).__init__(*args, **kwargs) 
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))
class addAgenciesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))
    class Meta:
        model=agencies
        fields='__all__'
    insurance=forms.BooleanField(required=False,label='Travel Insurance')
class addPlacesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))
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
class loginForm(forms.Form):
    username=forms.CharField(max_length=100,required=True,label='Username')
    password=forms.CharField(max_length=100,required=True,label='Password',widget=forms.PasswordInput())
    def __init__(self, *args, **kwargs):
        super(loginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Login'))
class signupForm(forms.Form):
    username=forms.CharField(max_length=100,required=True,label='Username')
    password=forms.CharField(max_length=100,required=True,label='Password',widget=forms.PasswordInput())
    email=forms.EmailField(max_length=100,required=True,label='Email')
    first_name=forms.CharField(max_length=100,required=True,label='First Name')
    last_name=forms.CharField(max_length=100,required=True,label='Last Name')
    def __init__(self, *args, **kwargs):
        super(signupForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Signup'))