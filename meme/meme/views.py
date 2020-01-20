from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.template.response import TemplateResponse
from django.views import View

class DefaultPages(View):

    template = "default/index.html"

    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, self.template)

    def post(self, request, *args, **kwargs):
        if request.POST.get('exit'):
            logout(request)
            return TemplateResponse(request, "default/index.html")
        return TemplateResponse(request, self.template)

def signup(request):

    uservalue = request.POST.get('username')
    passwordvalue = request.POST.get('password')
    if uservalue and passwordvalue:
        form = {'user': uservalue, 'pass': passwordvalue}
        try:
            user = User.objects.get(username=uservalue)
            context = {
                'form': form, 'error': 'The username you entered has already been taken. Please try another username.'}
            return render(request, 'default/signup.html', context)
        except User.DoesNotExist:
            user = User.objects.create_user(uservalue, password=passwordvalue)
            user.save()
            login(request, user)
            context = {'form': form}
            return redirect('/')
            # return render(request, 'default/index.html', context)
    else:
        #TODO fix GET request
        context = {'form': {'user': 'PFgjkyb', 'pass': 'asdasd'}}
        return render(request, 'default/signup.html', context)


def signin(request):

    uservalue = request.POST.get('username')
    passwordvalue = request.POST.get('password')
    form = {}
    if uservalue and passwordvalue:
        form = {'user': uservalue, 'pass': passwordvalue}
        user = authenticate(username=uservalue, password=passwordvalue)
        if user is not None:
            login(request, user)
            context = {'form': form}
            return redirect('/')
        else:
            context = {'form': form,
                       'error': 'The username and password combination is incorrect'}
            return render(request, 'default/signin.html', context)
    else:
        #TODO fix GET request
        context = {'form': {'user': 'PFgjkyb', 'pass': 'asdasd'}}
        return render(request, 'default/signin.html', context)
