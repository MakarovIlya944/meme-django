from django.core.management.base import BaseCommand, CommandError
from hookah.models import Recipe, Tobacco
import json


def __read_mixes(file):
    with open(file, 'r', encoding="utf-8") as f:
        data = json.load(f)
    return data


def __get_tobacco(data):
    if data.get("mark"):
        return {"mark": data["mark"], "taste": data["mark"]}
    return {"mark": "any", "taste": data["mark"]}


class Command(BaseCommand):
    help = 'Read recepies from file'

    def add_arguments(self, parser):
        parser.add_argument('mode', nargs='+', type=str)
        parser.add_argument('file', nargs='+', type=str)

    def handle(self, *args, **options):
        if args[2] == "read":
            data = __read_mixes(args[2])

            for r in data:
                tobac_list = []
                optional_list = []
                flask = "water"
                desc = ""
                for t in r["recipe"]:
                    t = __get_tobacco(t)
                    tobac_list.append(Tobacco(Mark=t["mark"], Taste=t["taste"]))
                if r.get("optional"):
                    for t in r["optional"]:
                        t = __get_tobacco(t)
                        optional_list.append(
                            Tobacco(Mark=t["mark"], Taste=t["taste"]))
                Recipe(TobaccoList=tobac_list, OptionalList=optional_list,
                    Flask=flask, Description=desc)

            self.stdout.write(self.style.SUCCESS(f'Added {len(data)} recipies'))
