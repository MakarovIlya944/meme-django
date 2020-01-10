from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from alias.sync import init, createTeam

class AliasSettings(View):

    def get(self, request, *args, **kwargs):
        init()
        return TemplateResponse(request, "alias/settings.html")

    def post(self, request, *args, **kwargs):
        team = request.POST.get('team')
        username = request.user.username
        createTeam(username, team)
        return TemplateResponse(request, "alias/settings.html")
