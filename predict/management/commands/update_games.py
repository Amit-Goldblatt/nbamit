from predict.models import Game, Team, Rtg_history
from nbamit.schedule_scraper import get_schedule
from datetime import datetime


def update_season():

    try:
        sc = get_schedule(datetime.now().year+1)
        se = datetime.now().year+1
    except:
        sc = get_schedule(datetime.now().year)
        se = datetime.now().year

    for index, row in sc.iterrows():
        if Game.objects.filter(date=row['DATE'], home_team__name=row['HOME'], away_team__name=row['VISITOR']).exists():
            a = Game.objects.get(date=row['DATE'], home_team__name=row['HOME'], away_team__name=row['VISITOR'])
            if row['HOME_PTS'] == None:
                a.home_score = row['HOME_PTS']
                a.away_score = row['VISITOR_PTS']
                a.save() 
            else:
                pass   
        else:
            home = Team.objects.get(name=row['HOME'])
            away = Team.objects.get(name=row['VISITOR'])
            a= Game(date=row['DATE'], home_team=home, away_team=away, home_score =  None, away_score = None, season = se)
            a.save()
       




    