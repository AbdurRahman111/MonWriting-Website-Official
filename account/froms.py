from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from . models import Profile

class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(
    label="Password",
    widget=forms.PasswordInput(attrs={'class':"form-control w-100 text-center mb-3", 'type':'password', 'placeholder':'***********'}),
    )
    password2 = forms.CharField(
    label="Password",
    widget=forms.PasswordInput(attrs={'class':"form-control w-100 text-center mb-3", 'type':'password', 'placeholder':'***********'}),
    )
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email',]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control w-100 text-center mb-3','placeholder':'User Name *'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control w-100 text-center mb-3','placeholder':'First Name *'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control w-100 text-center mb-3','placeholder':'Last Name *'}),
            'email': forms.TextInput(attrs={'class': 'form-control w-100 text-center mb-3','placeholder':'Email address...'}),
        }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control text-center'}),
            'email': forms.TextInput(attrs={'class': "form-control",'id':'inlineFormInputGroup','type':'email'}),
        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image','bio']
        widgets = {
            'bio':forms.Textarea(attrs={'class': 'form-control','placeholder':'Short Bio'}),
        }