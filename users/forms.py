from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserInfo


class UserForm(UserCreationForm):
    username = forms.CharField(widget= forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget= forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta():
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserInfoForm(forms.ModelForm):
    profile_pic = forms.FileField(required=False,label="Upload Profile Picture", widget=forms.FileInput(attrs={'class': 'form-control col-md-6'}))
    facebook_profile = forms.URLField(required=False,widget=forms.URLInput(attrs={'class': 'form-control col-md-6'}))
    class Meta():
        model = UserInfo
        fields = ['profile_pic', 'facebook_profile']