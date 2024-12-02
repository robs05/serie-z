from django.test import TestCase

from serie_zeta.models import Team, Player

class TeamTests(TestCase):
    def setUp(self):
        team = Team.objects.create(name="Team A", jersey_color="red", players_num_max=5)
        Player.objects.create(first_name="Antonio", last_name="Verdi", birth_date="2000-01-01",
                                position="Difensore", captain=False, jersey_number=3, team=team)
        Player.objects.create(first_name="Luigi", last_name="Bianchi", birth_date="2000-01-01",
                              position="Attaccante", captain=True, jersey_number=9, team=team)

    def test_delete_team(self):
        team = Team.objects.get(name="Team A")
        team.delete()
        self.assertEqual(team.is_deleted, True)
        self.assertEqual(Player.objects.filter(team=team).count(), 0)
        self.assertEqual(Team.objects.count(), 1)
        self.assertEqual(Player.objects.count(), 2)


