from django.core.management.base import BaseCommand, CommandError
from predict.models import Team, Game, Rtg_history
from nbamit.schedule_scraper import get_schedule
import pandas as pd
# class Command(BaseCommand):
#     help = 'populate schedule'

#     def add_arguments(self, parser):
#         pass

#     def handle(self, *args, **options):
        
#         schedule = get_schedule()
#         for game in schedule:
#             home_team = Team.objects.get(name=game['home_team'])
#             away_team = Team.objects.get(name=game['away_team'])
#             Game.objects.create(date=game['date'], home_team=home_team, away_team=away_team, home_score=game['home_score'], away_score=game['away_score'])
#         self.stdout.write(self.style.SUCCESS('Successfully populated db'))

class Command(BaseCommand):
    help = 'populate team'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        # df = get_schedule(2020)
        # team_names = [
        # 'Atlanta Hawks',
        # 'Boston Celtics',
        # 'Brooklyn Nets',
        # 'Charlotte Hornets',
        # 'Chicago Bulls',
        # 'Cleveland Cavaliers',
        # 'Dallas Mavericks',
        # 'Denver Nuggets',
        # 'Detroit Pistons',
        # 'Golden State Warriors',
        # 'Houston Rockets',
        # 'Indiana Pacers',
        # 'Los Angeles Clippers',
        # 'Los Angeles Lakers',
        # 'Memphis Grizzlies',
        # 'Miami Heat',
        # 'Milwaukee Bucks',
        # 'Minnesota Timberwolves',
        # 'New Orleans Pelicans',
        # 'New York Knicks',
        # 'Oklahoma City Thunder',
        # 'Orlando Magic',
        # 'Philadelphia 76ers',
        # 'Phoenix Suns',
        # 'Portland Trail Blazers',
        # 'Sacramento Kings',
        # 'San Antonio Spurs',
        # 'Toronto Raptors',
        # 'Utah Jazz',
        # 'Washington Wizards'
        # ]
        t = Team.objects.all()
        for team in t:
            team.delete()
        df = pd.read_csv('predict/teams_id team_name.csv')
        for index, row in df.iterrows():
            Team.objects.create(name=row['NICKNAME'], confrence=row['Conference'], rating=1500, rd=350, vol=0.06, id=row['TEAM_ID'])
            # save
        
