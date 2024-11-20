from django.test import TestCase

from serie_zeta.models import Team

class TeamTests(TestCase):
    def setUp(self):
        Team.objects.create(name="Team A", jersey_color="red", players_num_max=5)

    def test_team_name(self):
        team = Team.objects.get(name="Team A")
        self.assertEqual(team.name, "Team A")

    def test_team_jersey_color(self):
        team = Team.objects.get(name="Team A")
        self.assertEqual(team.jersey_color, "red")

    def test_team_players_num_max(self):
        team = Team.objects.get(name="Team A")
        self.assertEqual(team.players_num_max, 5)

    def test_team_str(self):
        team = Team.objects.get(name="Team A")
        self.assertEqual(str(team), "Team A")

    def test_team_delete(self):
        team = Team.objects.get(name="Team A")
        team.delete()
        self.assertEqual(team.is_deleted, True)