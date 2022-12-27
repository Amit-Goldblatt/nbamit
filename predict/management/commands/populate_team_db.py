from django.core.management.base import BaseCommand, CommandError
from predict.models import Team
import pandas as pd

# this command is used to populate the team database for the first time.
# it creates a team object for each team in the csv file.
class Command(BaseCommand):
    help = 'populate team'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        
        t = Team.objects.all()
        for team in t:
            team.delete()
        df = pd.read_csv('predict/teams_id team_name.csv')
        for index, row in df.iterrows():
            Team.objects.create(name=row['NICKNAME'], confrence=row['Conference'], rating=1500, rd=350, vol=0.06, id=row['TEAM_ID'])
            
        
