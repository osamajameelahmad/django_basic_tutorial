from django.core.management.base import BaseCommand, CommandError
from random import randint


class Command(BaseCommand):
    help = 'Help to get random number'

    def add_arguments(self, parser):
        parser.add_argument('max_number', type=int)

    def handle(self, *args, **options):
        # print(options)
        try:
            number = randint(0, int(options['max_number']))
        except Exception as e:
            raise CommandError(str(e))
        self.stdout.write(self.style.SUCCESS('Random number created is: "%s"' % number))
