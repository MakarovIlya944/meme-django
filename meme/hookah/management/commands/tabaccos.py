from django.core.management.base import BaseCommand, CommandError
from hookah.models import Recipe, Tabacco
import json


def read_mixes(file):
    with open(file, 'r', encoding="utf-8") as f:
        data = json.load(f)
    return data


def construct_tobacco(data):
    if type(data) == str:
        taste = data
        mark = None
    else:
        taste = data.get('taste')
        mark = data.get('mark')
    try:
        return Tabacco.objects.get(Taste=taste, Mark=mark)
    except Exception:
        Tabacco(Mark=mark, Taste=taste).save()
    return Tabacco.objects.get(Taste=taste, Mark=mark)


class Command(BaseCommand):
    help = 'Read recepies from file'

    def add_arguments(self, parser):
        parser.add_argument('mode', nargs='+', type=str)
        parser.add_argument('file', nargs='+', type=str)
        parser.add_argument('--my',
            action='store_true',
            dest='my',
            default=False)

    def handle(self, *args, **options):
        print(options)
        if options["mode"][0] == "read":
            data = read_mixes(options["file"][0])
            if options["my"]:
                i = 0
                for r in data:
                    t = construct_tobacco(r)
                    t.Have = True
                    t.save()
                self.stdout.write(self.style.SUCCESS(
                    f'Added {len(data)} tabaccos'))
            else:
                i = len(Recipe.objects.all())
                for r in data:
                    i += 1
                    try:
                        tobac_list = []
                        optional_list = []
                        flask = "water"
                        desc = ""
                        for t in r["recipe"]:
                            # R.TabaccoList.add(construct_tobacco(t))
                            tobac_list.append(construct_tobacco(t)[0])
                        R = Recipe.objects.create(RecipeId=i, Flask=r.get(
                            'flask') or flask, Description=r.get('description') or desc)
                        R.TabaccoList.set(tobac_list)
                        if r.get("optional"):
                            for t in r["optional"]:
                                optional_list.append(construct_tobacco(t)[0])
                        R.OptionalList.set(optional_list)
                        R.save()
                    except Exception as ex:
                        print(ex.args)

                self.stdout.write(self.style.SUCCESS(
                    f'Added {len(data)} recipies'))
