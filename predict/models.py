from django.db import models
from nbamit import rtg_utils
import random
# Create your models here.
class Team(models.Model):

    id  = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    confrence = models.CharField(max_length=100)
    rating = models.FloatField(null=True)
    rd = models.FloatField(null=True)
    vol = models.FloatField(null=True)
    def __str__(self):
        return f"name:{self.name} rating{self.rating} rd{self.rd} volatility {self.vol}"
    


class Game(models.Model):
   
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_team')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_team')
    home_score = models.IntegerField(null=True, )
    away_score = models.IntegerField(null=True)
    winner = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='winner', null=True)
    odds = models.FloatField(null=True)
    predicted_winner = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='predicted_winner', null=True)
    season = models.IntegerField(null = True)
    
    def calc(self):       
        # check if home and away scores are not null
        if self.home_score is not None and self.away_score is not None:
            # check if home team won
            if self.home_score > self.away_score:
                self.winner = self.home_team
                
               
            # check if away team won
            elif self.away_score > self.home_score:
                self.winner = self.away_team
            self.save()
            

                # save Rtg_history
            print(self.home_team, self.away_team)
            Rtg_history.objects.create(team=self.home_team, rtg=self.home_team.rating, date=self.date)
            Rtg_history.objects.create(team=self.away_team, rtg=self.away_team.rating, date=self.date)
           
            # calculate new ratings
            home_team_rating, home_team_rd,home_team_vol = rtg_utils.calc_new_rating(self.home_team, self.away_team, self.winner)
            away_team_rating, away_team_rd,away_team_vol  = rtg_utils.calc_new_rating(self.away_team, self.home_team, self.winner)
        
            # update ratings
            self.home_team.rating = home_team_rating
            self.home_team.rd = home_team_rd
            self.home_team.vol = home_team_vol
            self.away_team.rating = away_team_rating
            self.away_team.rd = away_team_rd
            self.away_team.vol = away_team_vol

            self.home_team.save()
            self.away_team.save()

        # simulate game
        else:
            self.odds = rtg_utils.predict_winner(self.home_team, self.away_team)
            winner_temp =  random.choices([self.home_team ,self.away_team],[self.odds,1-self.odds])
            self.predicted_winner = winner_temp[0]
            self.save()
    


class Rtg_history(models.Model):
    id = models.AutoField(primary_key=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    rtg = models.FloatField()
    date = models.DateField()

