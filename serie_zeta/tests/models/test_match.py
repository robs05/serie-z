from django.test import TestCase

from serie_zeta.models import Match, Team, Placement, Tournament

class MatchTests(TestCase):
    def setUp(self):
        home_team = Team.objects.create(name="Team A", jersey_color="red", players_num_max=5)
        away_team = Team.objects.create(name="Team B", jersey_color="blue", players_num_max=5)

        Match.objects.create(home_team=home_team, away_team=away_team, home_team_goals=1, away_team_goals=1,
                             match_date="2021-06-01")

    def test_match_str(self):
        match = Match.objects.get(home_team__name="Team A")
        self.assertEqual(str(match), "Team A(1) vs Team B(1) - 2021-06-01 00:00:00+00:00")