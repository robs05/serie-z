from django.test import TestCase
from django.urls import reverse
from serie_zeta.models import Tournament, Team, TournamentParticipation

class TournamentIdViewTests(TestCase):
    def setUp(self):
        self.tournament = Tournament.objects.create(name="Tournament A", code="T1", description="Description",
                                                    start_date="2021-06-01", end_date="2021-06-30")
        self.teamA = Team.objects.create(name="Team A", jersey_color="red", players_num_max=5)
        self.teamB = Team.objects.create(name="Team B", jersey_color="blue", players_num_max=5)
        self.participation = TournamentParticipation.objects.create(team=self.teamA, tournament=self.tournament)
        self.participation = TournamentParticipation.objects.create(team=self.teamB, tournament=self.tournament)
    def test_tournament_id_view(self):
        response = self.client.get(reverse('serie_zeta:tournament', args=[self.tournament.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'serie_zeta/tournament.html')
        self.assertContains(response, self.tournament.name)
        self.assertEqual(response.context['tournament'].name, self.tournament.name)
        self.assertEqual(response.context['teams'][0].team.name, self.teamA.name)
        self.assertEqual(response.context['teams'].count(),2)


