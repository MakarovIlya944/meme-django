from django import forms
from default import models

class Signupform(forms.ModelForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    
    class Meta:
        model = models.User
        fields = ["username", "password"]
