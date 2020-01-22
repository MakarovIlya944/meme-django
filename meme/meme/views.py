from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.template.response import TemplateResponse
from django.views import View


class DefaultPages(View):

    template = "default/index.html"
    mode = 'signin'

    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, self.template)

    def post(self, request, *args, **kwargs):
        if request.POST.get('exit'):
            logout(request)
            return TemplateResponse(request, self.template)

        uservalue = request.POST.get('username')
        passwordvalue = request.POST.get('password')
        if uservalue and passwordvalue:
            if self.mode == 'signin':
                user = authenticate(username=uservalue, password=passwordvalue)
                if user is not None:
                    login(request, user)
                    return redirect('/')
                else:
                    context = {
                        'error': 'The username and password combination is incorrect'}
                    return TemplateResponse(request, self.template, context=context)
            elif self.mode == 'signup':
                try:
                    user = User.objects.get(username=uservalue)
                    context = {
                        'error': 'The username you entered has already been taken. Please try another username.'}
                    return TemplateResponse(request, self.template, context=context)
                except Exception:#User.DoesNotExist:
                    user = User.objects.create_user(
                        uservalue, password=passwordvalue)
                    user.save()
                    login(request, user)
                    return redirect('/')
        return TemplateResponse(request, self.template)
