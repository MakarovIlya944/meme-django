from django.shortcuts import render
from default import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, "default/index.html")

def signup(request):
    return render(request, "default/signup.html")

def signin(request):
  
    uservalue=''
    passwordvalue=''

    form= forms.Loginform(request.POST or None)
    if form.is_valid():
        uservalue= form.cleaned_data.get("username")
        passwordvalue= form.cleaned_data.get("password")

        user= authenticate(username=uservalue, password=passwordvalue)
        if user is not None:
            login(request, user)
            context= {'form': form,
                      'error': 'The login has been successful'}
            
            return render(request, 'default/signin.html', context)
        else:
            context= {'form': form,
                      'error': 'The username and password combination is incorrect'}
            
            return render(request, 'default/signin.html', context )

    else:
        context= {'form': form}
        return render(request, 'default/signin.html', context)
