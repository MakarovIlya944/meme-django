from django.template.response import TemplateResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

def index(request):
    return TemplateResponse(request, "alias/index.html")

class AliasIndex(View):

    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, "alias/index.html")

    def post(self, request, *args, **kwargs):
        t = 'sdas'
        team = request.POST.get('team')
        return TemplateResponse(request, "alias/index.html")