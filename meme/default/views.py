from django.shortcuts import render
from default import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, "default/index.html")

def signup(request):

    uservalue=''
    passwordvalue=''

    form = forms.Signupform(request.POST or None)
    if form.is_valid():
        fs = form.save(commit=False)
        uservalue = form.cleaned_data.get("username")
        passwordvalue = form.cleaned_data.get("password")
        try:
            user= User.objects.get(username=uservalue) #if able to get, user exists and must try another username
            context= {'form': form, 'error':'The username you entered has already been taken. Please try another username.'}
            return render(request, 'default/signup.html', context)
        except User.DoesNotExist:
            user= User.objects.create_user(uservalue, password= passwordvalue)
            user.save()
            login(request,user)

            fs.user= request.user
            fs.save()
            context= {'form': form}
            return render(request, 'default/index.html', context)
    else:
        context= {'form': form}
        return render(request, 'default/signup.html', context)

def signin(request):
  
    uservalue=''
    passwordvalue=''

    form = forms.Signupform(request.POST or None)
    if form.is_valid():
        uservalue= form.cleaned_data.get("username")
        passwordvalue= form.cleaned_data.get("password")

        user= authenticate(username=uservalue, password=passwordvalue)
        if user is not None:
            login(request, user)
            context= {'form': form,
                      'user': uservalue}
            
            return render(request, 'default/index.html', context)
        else:
            context= {'form': form,
                      'error': 'The username and password combination is incorrect'}
            
            return render(request, 'default/signin.html', context )

    else:
        context= {'form': form}
        return render(request, 'default/signin.html', context)
