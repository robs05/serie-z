from django.urls import reverse
from django.test import TestCase
from serie_zeta.models import Team
from django.contrib.auth.models import User

# test the view new_team
class CreateNewTeamTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='P@ssw0rd')
        self.client.login(username='user1', password='P@ssw0rd')
    def test_create_new_team(self):
        response = self.client.get(reverse('serie_zeta:new_team'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'serie_zeta/new_team.html')
        response = self.client.post(reverse('serie_zeta:new_team'),
                                    {'name': 'Team A', 'jersey_color': 'red', 'players_num_max': 5})
        self.assertEqual(response.status_code, 302)

        teams = Team.objects.all()
        self.assertEqual(teams.count(), 1)
        team = teams[0]
        self.assertEqual(team.name, 'Team A')
        self.assertEqual(team.jersey_color, 'red')
        self.assertEqual(team.players_num_max, 5)