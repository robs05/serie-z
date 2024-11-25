from django.test import TestCase
from datetime import date

from serie_zeta.models import TournamentParticipation, Team, Tournament

class TournamentParticipationWithMoreTeamsTests(TestCase):
    def setUp(self):
        team = Team.objects.create(name="A", jersey_color="Red", players_num_max=8)
        team2 = Team.objects.create(name="B", jersey_color="Blue", players_num_max=8)
        team3 = Team.objects.create(name="C", jersey_color="Green", players_num_max=8)
        team4 = Team.objects.create(name="D", jersey_color="Yellow", players_num_max=8)

        tournament = Tournament.objects.create(name="Torneo di calcio", code="T001",  description="Torneo di calcio amatoriale",
                                               start_date="2021-06-01", end_date="2021-06-30")

        TournamentParticipation.objects.create(team=team, tournament=tournament)
        TournamentParticipation.objects.create(team=team2, tournament=tournament)
        TournamentParticipation.objects.create(team=team3, tournament=tournament)
        TournamentParticipation.objects.create(team=team4, tournament=tournament)

    def test_tournament_teams(self):
        tournament = Tournament.objects.get(code="T001")
        self.assertEqual(tournament.teams.count(), 4)

    def test_delete_team(self):
        team = Team.objects.get(name="A")
        team.delete()
        tournament = Tournament.objects.get(code="T001")
        # filter the teams that are not deleted
        self.assertEqual(tournament.teams.filter(is_deleted=False).count(), 3)

    def test_delete_tournament(self):
        tournament = Tournament.objects.get(code="T001")
        tournament.delete()
        self.assertEqual(Tournament.objects.all().count(), 0)
        teams = Team.objects.all()
        # filter the teams that are not deleted
        self.assertEqual(teams.filter(is_deleted=False).count(), 4)