from django.test import TestCase
from .models import Team, Game, Rtg_history
# Create your tests here.
class TeamTestCase(TestCase):
    def setUp(self):
        Team.objects.create(name='amit', confrence='east', rating=1500, rd=350, vol=0.06)
        Team.objects.create(name='amit2', confrence='east', rating=1400, rd=30, vol=0.06)
    def test_team(self):
        amit = Team.objects.get(name='amit')
        amit2 = Team.objects.get(name='amit2')
        self.assertEqual(amit.name, 'amit')
        self.assertEqual(amit2.name, 'amit2')
        self.assertEqual(amit.rating, 1500)
        self.assertEqual(amit2.rating, 1400)
        self.assertEqual(amit.rd, 350)
        self.assertEqual(amit2.rd, 30)
        self.assertEqual(amit.vol, 0.06)
        self.assertEqual(amit2.vol, 0.06)
        self.assertEqual(amit.confrence, 'east')
        self.assertEqual(amit2.confrence, 'east')
class GameTestCase(TestCase):
    def setUp(self):
        amit = Team.objects.create(name='amit', confrence='east', rating=3000, rd=350, vol=0.06)
        amit2 = Team.objects.create(name='amit2', confrence='east', rating=2000, rd=30, vol=0.06)
        Game.objects.create(date='2020-01-01', home_team=amit, away_team=amit2, home_score=100, away_score=90)
        Game.objects.create(date='2020-01-02', home_team=amit, away_team=amit2, home_score=None, away_score=None)
    def test_game(self):
        amit = Team.objects.get(name='amit')
        amit2 = Team.objects.get(name='amit2')
        game1 = Game.objects.get(date='2020-01-01')
        game2 = Game.objects.get(date='2020-01-02')
        game1.calc()
        game2.calc()
        self.assertEqual(game1.home_team, amit)
        self.assertEqual(game1.away_team, amit2)
        self.assertEqual(game1.home_score, 100)
        self.assertEqual(game1.away_score, 90)
        self.assertEqual(game1.winner, amit)
        self.assertEqual(game1.predicted_winner, None)
        counter =0
        for i in range(50):
            game2.calc()
            if game2.predicted_winner == amit:
                counter += 1
        self.assertGreater(counter, 25)
        self.assertEqual(game2.away_team, amit2)
        self.assertEqual(game2.home_score, None)
        self.assertEqual(game2.away_score, None)
        self.assertEqual(game2.winner, None)
        self.assertEqual(game2.predicted_winner, amit)
