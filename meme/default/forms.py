from django import forms
from default import models

class Signupform(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    
    class Meta:
        model= models.Siteuser
        fields= ["username", "password"]
