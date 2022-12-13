from django import forms
from .models import newUser

class newuserForm(forms.ModelForm):
    class Meta:
        model=newUser
        fields='__all__'