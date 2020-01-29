from django.template.response import TemplateResponse
from django.views import View
from alias.sync import clientInit, startGame

class AliasSettings(View):

    template = "alias/settings.html"

    def get(self, request, *args, **kwargs):
        clientInit('http://localhost:5000')
        if self.template == "alias/game.html":
            startGame()
        return TemplateResponse(request, self.template)
