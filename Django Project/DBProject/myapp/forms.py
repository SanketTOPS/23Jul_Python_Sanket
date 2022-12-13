from dataclasses import fields
from pyexpat import model
from django import forms
from .models import user_signup

class userForm(forms.ModelForm):
    class Meta:
        model=user_signup
        fields='__all__'
        #fields=['name','email','password']

class updateUser(forms.ModelForm):
    class Meta:
        model=user_signup
        fields=['name','email','password','mobile']