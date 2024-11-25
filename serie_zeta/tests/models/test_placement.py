from django.test import TestCase

from serie_zeta.models import Placement, Team

class PlacementTests(TestCase):
    def setUp(self):
        team = Team.objects.create(name="Team A", jersey_color="red", players_num_max=5)
        team1 = Team.objects.create(name="Team B", jersey_color="blue", players_num_max=5)
        Placement.objects.create(team=team, placement_code="T001", points=3, goal_difference=2, goals_scored=3,
                                  goals_conceded=1, matches_played=1, matches_won=1, matches_drawn=0, matches_lost=0)
        Placement.objects.create(team=team1, placement_code="T001", points=0, goal_difference=-2, goals_scored=1,
                                    goals_conceded=3, matches_played=1, matches_won=0, matches_drawn=0, matches_lost=1)

    def test_placement_teams(self):
        placements = Placement.objects.filter(placement_code="T001")
        self.assertEqual(placements.count(), 2)

    def test_placement_str(self):
        placement = Placement.objects.get(team__name="Team A")
        self.assertEqual(str(placement), "Team A - T001 - 3 points")