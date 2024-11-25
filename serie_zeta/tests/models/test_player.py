from django.test import TestCase

from serie_zeta.models import Player, Team
from django.contrib.auth.models import User

class PlayerTests(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="user", password="password")
        team = Team.objects.create(name="Team A", jersey_color="red", players_num_max=5)
        Player.objects.create(user=user, first_name="A", last_name="B", birth_date="2000-01-01",
                              position="Portiere", captain=False, jersey_number=4, team=team)

    def test_player_first_name(self):
        player = Player.objects.get(first_name="A")
        self.assertEqual(player.first_name, "A")

    def test_player_position(self):
        player = Player.objects.get(first_name="A")
        self.assertEqual(player.position, "Portiere")

    def test_player_str(self):
        player = Player.objects.get(first_name="A")
        self.assertEqual(str(player), "A B")