from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from alias.sync import createTeam

class AliasSettings(View):

    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, "alias/settings.html")
