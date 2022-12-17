from django.core.management.base import BaseCommand, CommandError
from predict.models import Game, Team, Rtg_history
from nbamit.schedule_scraper import get_schedule
from datetime import datetime

class Command(BaseCommand):
    help = 'update_games'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # get season
        try:
            sc = get_schedule(datetime.now().year+1)
            se = datetime.now().year+1
        except:
            sc = get_schedule(datetime.now().year)
            se = datetime.now().year
# update new scores
        for index, row in sc.iterrows():
            if Game.objects.filter(date=row['DATE'], home_team__name=row['HOME'], away_team__name=row['VISITOR']).exists():
                a = Game.objects.get(date=row['DATE'], home_team__name=row['HOME'], away_team__name=row['VISITOR'])
                if row['HOME_PTS'] == None:
                    a.home_score = row['HOME_PTS']
                    a.away_score = row['VISITOR_PTS']
                    a.save() 
                else:
                    pass   
            # add new games
            else:
                home = Team.objects.get(name=row['HOME'])
                away = Team.objects.get(name=row['VISITOR'])
                a= Game(date=row['DATE'], home_team=home, away_team=away, home_score =  None, away_score = None, season = se)
                a.save()

        t = Team.objects.all()
        for team in t:
            team.rating=1500
            team.rd=350
            team.vol=0.06
        h= Rtg_history.objects.all()
        for hist in h:
            hist.delete()
        g = Game.objects.all()
        for game in g:
            game.calc()