from django import forms 
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['username', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class PostCommentsForm(forms.ModelForm):
    
    class Meta:
        model = PostComment
        fields = ["body"]

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'image']
        widgets = {
            
            'bio': forms.Textarea(attrs={'required': False}),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug','image','body',]
        widgets = {
            
            'body': forms.Textarea(attrs={'required': True}),
        }


class SearchPostForm(forms.Form):
    search = forms.CharField(label='Search For a Post')


