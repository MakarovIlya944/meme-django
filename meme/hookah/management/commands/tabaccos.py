from django.core.management.base import BaseCommand, CommandError
from hookah.models import Recipe, Tobacco
import json


def __read_mixes(file):
    with open(file, 'r', encoding="utf-8") as f:
        data = json.load(f)
    return data


def construct_tobacco(data):
    if type(data) == str:  # t.get('mark'):
        tobacco = Tobacco(Mark=data)
    else:
        tobacco = Tobacco(Mark=data.get('mark'), Taste=data.get('taste'))
    tobacco.save()
    return tobacco


class Command(BaseCommand):
    help = 'Read recepies from file'

    def add_arguments(self, parser):
        parser.add_argument('mode', nargs='+', type=str)
        parser.add_argument('file', nargs='+', type=str)

    def handle(self, *args, **options):
        tobacco = Tobacco(Mark="a", Taste="a")
        tobacco.save()
        print(tobacco)
        if options["mode"] == "read":
            data = __read_mixes(options["file"])

            for r in data:
                tobac_list = []
                optional_list = []
                flask = "water"
                desc = ""
                for t in r["recipe"]:
                    tobac_list.append(construct_tobacco(t))
                R = Recipe(tobaccoList=tobac_list)
                R.Flask = r.get('flask') or flask
                R.Description = r.get('description') or desc
                if r.get("optional"):
                    for t in r["optional"]:
                        optional_list.append(construct_tobacco(t))
                R.OptionalList = optional_list
                R.save()

            self.stdout.write(self.style.SUCCESS(f'Added {len(data)} recipies'))
