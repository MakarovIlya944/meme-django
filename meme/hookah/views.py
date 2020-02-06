from django.views import View
from django.template.response import TemplateResponse
from hookah.models import Recipe, Tabacco

# Create your views here.


class HookahIndex(View):

    store = [
        {'mark': 'nachla', 'taste': 'mint'},
        {'mark': 'nachla', 'taste': 'strabwerry'},
        {'mark': 'nachla', 'taste': 'pin'},
    ]

    def get(self, request, *args, **kwargs):
        a = Recipe.objects.all()
        recepies = [{'tobaccos': [{'taste':str(t),'have':'list-group-item-primary' if t.Have else 'list-group-item-danger'} for t in e.TabaccoList.all()], 'value': e.price()}
                    for e in a]
        recepies = sorted(recepies, key=lambda x: -x['value'])
        return TemplateResponse(request, "hookah/index.html", context={'store': self.store, 'recepies': recepies})

