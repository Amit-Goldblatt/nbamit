from django.core.management.base import BaseCommand, CommandError
from predict.models import Game, Team, Rtg_history
from nbamit.schedule_scraper import get_schedule
from datetime import datetime
import pandas as pd
# this command is the main command that is used to update the database with new scores or new games.
# it is run every day at 12:00 utc by the heroku scheduler
class Command(BaseCommand):
    help = 'update_games'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # # this part is used to check if the schedule for the next season is available
        try:
            sc = get_schedule(datetime.now().year+1)
            se = datetime.now().year+1
            
        except:
            sc = get_schedule(datetime.now().year)
            se = datetime.now().year

        # remove all games from the schedule
        Game.objects.all().delete()
        for index, row in sc.iterrows():          
            home = Team.objects.get(name=row['HOME'])
            away = Team.objects.get(name=row['VISITOR'])
            a= Game(date=row['DATE'], home_team=home, away_team=away, home_score =  None, away_score = None, season = se)
            a.save()
        # #  check if game is already in database  
        #     if Game.objects.filter(date=row['DATE'], home_team__name=row['HOME'], away_team__name=row['VISITOR']).exists():
        #         # fetch game from database
        #         a = Game.objects.get(date=row['DATE'], home_team__name=row['HOME'], away_team__name=row['VISITOR'])
                
        #         # if game dosen't have a score yet, skips it.
        #         if pd.isnull(row['VISITOR_PTS']):
        #             continue
        #         # if game has a score, update it.
        #         else:
        #             print(row['HOME_PTS'], 1)
        #             a.home_score = row['HOME_PTS']
        #             print("q")
        #             a.away_score = row['VISITOR_PTS']
        #             print("update worked")
        #             a.save()  
        #             print("e")  
        #     # add new games
        #     else:
                
        #         home = Team.objects.get(name=row['HOME'])
        #         away = Team.objects.get(name=row['VISITOR'])
        #         a= Game(date=row['DATE'], home_team=home, away_team=away, home_score =  None, away_score = None, season = se)
        #         a.save()
                
        # update ratings 
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