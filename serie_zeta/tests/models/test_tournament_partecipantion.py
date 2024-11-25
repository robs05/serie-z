from django.test import TestCase
from datetime import date

from serie_zeta.models import TournamentParticipation, Team, Tournament

class TournamentParticipationTests(TestCase):
    def setUp(self):
        team = Team.objects.create(name="A", jersey_color="Red", players_num_max=8)
        tournament = Tournament.objects.create(name="Torneo di calcio", description="Torneo di calcio amatoriale",
                                               start_date="2021-06-01", end_date="2021-06-30")

        TournamentParticipation.objects.create(team=team, tournament=tournament)

    def test_tournament_participation_team(self):
        tournament_participation = TournamentParticipation.objects.get(team__name="A")
        self.assertEqual(tournament_participation.team.name, "A")

    def test_tournament_participation_tournament(self):
        tournament_participation = TournamentParticipation.objects.get(team__name="A")
        self.assertEqual(tournament_participation.tournament.name, "Torneo di calcio")

    def test_tournament_participation_participation_date(self):
        tournament_participation = TournamentParticipation.objects.get(team__name="A")
        self.assertEqual(tournament_participation.participation_date.strftime("%Y-%m-%d"), date.today().strftime("%Y-%m-%d"))

    def test_tournament_participation_str(self):
        tournament_participation = TournamentParticipation.objects.get(team__name="A")
        self.assertEqual(str(tournament_participation), "A in Torneo di calcio - " + date.today().strftime("%Y-%m-%d"))

    # create a tounamnent with three teams and check if the number of teams is correct
    def test_tournament_teams(self):
        tournament = Tournament.objects.get(name="Torneo di calcio")
        self.assertEqual(tournament.teams.count(), 1)