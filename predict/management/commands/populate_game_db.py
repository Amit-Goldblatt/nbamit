from django.core.management.base import BaseCommand, CommandError
from predict.models import Team, Game, Rtg_history
from nbamit.schedule_scraper import get_schedule
import pandas as pd
class Command(BaseCommand):
    help = 'populate schedule'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        
        df = get_schedule(2022)
        b = Game.objects.all()
        for game in b:
            game.delete()
        
        for index, row in df.iterrows():
            home = Team.objects.get(name=row['HOME'])
            away = Team.objects.get(name=row['VISITOR'])
            try:
                a = Game(date=row['DATE'], home_team=home, away_team=away, home_score=row['HOME_PTS'], away_score=row['VISITOR_PTS'], season = 2022)
                a.save()
            except:
                a= Game(date=row['DATE'], home_team=home, away_team=away, home_score =  None, away_score = None, season = 2022)
                a.save()
            
        df = get_schedule(2023)     
        
        for index, row in df.iterrows():
            home = Team.objects.get(name=row['HOME'])
            away = Team.objects.get(name=row['VISITOR'])
            try:
                a = Game(date=row['DATE'], home_team=home, away_team=away, home_score=row['HOME_PTS'], away_score=row['VISITOR_PTS'], season = 2023)
                a.save()
            except:
                a= Game(date=row['DATE'], home_team=home, away_team=away, home_score =  None, away_score = None, season = 2023)
                a.save()
        self.stdout.write(self.style.SUCCESS('Successfully populated db'))