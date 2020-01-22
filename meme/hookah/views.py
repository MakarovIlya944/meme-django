from django.views import View
from django.template.response import TemplateResponse

# Create your views here.


class HookahIndex(View):

    store = [
        {'mark': 'nachla', 'taste': 'mint'},
        {'mark': 'nachla', 'taste': 'strabwerry'},
        {'mark': 'nachla', 'taste': 'pin'},
    ]

    def get(self, request, *args, **kwargs):
        return TemplateResponse(request, "hookah/index.html", context={'store': self.store})
