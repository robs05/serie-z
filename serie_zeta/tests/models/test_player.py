from django.test import TestCase

from serie_zeta.models import Player, Team
from django.contrib.auth.models import User

class PlayerTests(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="antonioverdi", password="password")
        team = Team.objects.create(name="Team A", jersey_color="red", players_num_max=5)
        Player.objects.create(user=user, first_name="Antonio", last_name="Verdi", birth_date="2000-01-01",
                              position="Portiere", captain=False, jersey_number=1, team=team)

    def test_player_first_name(self):
        player = Player.objects.get(first_name="Antonio")
        self.assertEqual(player.first_name, "Antonio")

    def test_player_position(self):
        player = Player.objects.get(first_name="Antonio")
        self.assertEqual(player.position, "Portiere")

    def test_player_str(self):
        player = Player.objects.get(first_name="Antonio")
        self.assertEqual(str(player), "Antonio Verdi Portiere 1")

    # se viene eliminato un giocatore dalla squadra non bidsogna cancellare il team
    def test_player_delete(self):
        player = Player.objects.get(first_name="Antonio")
        player.delete()
        self.assertEqual(Player.objects.count(), 0)
        self.assertEqual(Team.objects.count(), 1)