from django.forms import forms
from django.forms import ModelForm
from .models import Blog,Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
CRISPY_TEMPLATE_PACK = 'bootstrap4'
class BlogForm(ModelForm):
    class Meta:
        model=Blog
        fields=['caption','picture','User']
        wigits={
            'User':forms.HiddenInput()
        }
    def __init__(self,*args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self) 
        self.helper.add_input(Submit('submit', 'Submit'))
class CommentForm(ModelForm):
    class Meta:
        model=Comment
        fields=['comment','blog','User']
        wigits={
            'User':forms.HiddenInput(),
            'blog':forms.HiddenInput()
        }
    def __init__(self,*args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self) 
        self.helper.add_input(Submit('submit', 'Submit'))