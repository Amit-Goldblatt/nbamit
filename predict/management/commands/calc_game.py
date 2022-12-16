from django.core.management.base import BaseCommand, CommandError
from predict.models import Team, Game, Rtg_history
from nbamit.schedule_scraper import get_schedule
import pandas as pd
class Command(BaseCommand):
    help = 'populate schedule'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        h = Rtg_history.objects.all()
        for hist in h:
            hist.delete()
        g = Game.objects.all()
        for game in g:
                game.calc()
        
        self.stdout.write(self.style.SUCCESS('Successfully populated db'))