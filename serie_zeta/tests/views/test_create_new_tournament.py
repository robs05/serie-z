from django.test import TestCase
from django.urls import reverse
from serie_zeta.models import Tournament, Team, TournamentParticipation
from django.contrib.auth.models import User



class CreateNewTournamentTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='P@ssw0rd')
        self.client.login(username='user1', password='P@ssw0rd')

    def test_create_new_tournament(self):
        response = self.client.get(reverse('serie_zeta:new_tournament'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'serie_zeta/new_tournament.html')

        response = self.client.post(reverse('serie_zeta:new_tournament'),
                                    {'name': 'Torneo A', 'code':'1234', 'description':'aaaaa',
                                     'start_date': '2020-01-01', 'end_date': '2020-12-31'}, follow=True)

        if response.context and 'form' in response.context:
            form = response.context['form']
            if not form.is_valid():
                print(form.errors)

        self.assertEqual(response.status_code, 200)

        tournaments = Tournament.objects.all()
        self.assertEqual(tournaments.count(), 1)
        tournament = tournaments[0]
        self.assertEqual(tournament.name, 'Torneo A')
        self.assertEqual(tournament.code, '1234')
        self.assertEqual(tournament.description, 'aaaaa')
        self.assertEqual(tournament.start_date.strftime('%Y-%m-%d'), '2020-01-01')

        tournament_participations = TournamentParticipation.objects.all()
        self.assertEqual(tournament_participations.count(), 0)

        teams = Team.objects.all()
        self.assertEqual(teams.count(), 0)