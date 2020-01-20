from django.template.response import TemplateResponse
from django.views import View
from alias.sync import clientInit

class AliasSettings(View):

    def get(self, request, *args, **kwargs):
        clientInit('http://localhost:5000')
        return TemplateResponse(request, "alias/settings.html")
