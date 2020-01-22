from django.core.management.base import BaseCommand, CommandError
from hookah.models import Recipe, Tobacco
import json

def __read_mixes(file):
    with open(file, 'r') as f:
        data = json.load(f)
    return data

class Command(BaseCommand):
    help = 'Read recepies from file'

    def add_arguments(self, parser):
        parser.add_argument('file', nargs='+', type=str)

    def handle(self, *args, **options):

        data = __read_mixes(args[1])

        for r in data:
            if type() == str:
                t = Tobacco(Mark=)
            Recipe()

        for poll_id in options['poll_id']:
            try:
                poll = Poll.objects.get(pk=poll_id)
            except Poll.DoesNotExist:
                raise CommandError('Poll "%s" does not exist' % poll_id)

            poll.opened = False
            poll.save()

            self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))