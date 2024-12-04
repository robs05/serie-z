from django.test import TestCase
from django.utils import timezone

from serie_zeta.models import Team, Player, User
from serie_zeta.models import Tournament, TournamentParticipation
from serie_zeta.models import Match, Placement, Referee

class TeamTests(TestCase):
    def setUp(self):
        team1 = Team.objects.create(name="Team A", jersey_color="red", players_num_max=5)
        team2 = Team.objects.create(name="Team B", jersey_color="blue", players_num_max=5)
        user1 = User.objects.create_user(username="antonioverdi", password="password")
        Player.objects.create(user=user1, first_name="Antonio", last_name="Verdi", birth_date="2000-01-01",
                                position="Difensore", captain=False, jersey_number=3, team=team1)
        user2 = User.objects.create_user(username="luigibianchi", password="password")
        Player.objects.create(user=user2, first_name="Luigi", last_name="Bianchi", birth_date="2000-01-01",
                              position="Attaccante", captain=True, jersey_number=9, team=team1)

        tournament = Tournament.objects.create(name="Torneo di calcio", code="T2021",
                                               description="Torneo di calcio amatoriale",
                                               start_date="2021-06-01", end_date="2021-06-30")

        TournamentParticipation.objects.create(team=team1, tournament=tournament)
        TournamentParticipation.objects.create(team=team2, tournament=tournament)

        user3 = User.objects.create_user(username="mariorossi", password="password")
        referee = Referee.objects.create(user=user3, first_name="Mario", last_name="Rossi", birth_date="1990-01-01")

        Match.objects.create(home_team=team1, away_team=team2, match_date=timezone.make_aware(timezone.datetime(2021, 6, 1, 15, 0)),
                                     home_team_goals=2, away_team_goals=1, referee=referee)
        Match.objects.create(home_team=team2, away_team=team1, match_date=timezone.make_aware(timezone.datetime(2022, 6, 1, 15, 0)),
                             home_team_goals=2, away_team_goals=2, referee=referee)

        Placement.objects.create(team=team1, placement_code="CL1", points=4, goal_difference=1, goals_scored=4,
                                 goals_conceded=3, matches_played=2, matches_won=1, matches_drawn=1, matches_lost=0)
        Placement.objects.create(team=team2, placement_code="CL1", points=1, goal_difference=-1, goals_scored=3
                                 , goals_conceded=4, matches_played=2, matches_won=0, matches_drawn=1, matches_lost=1)


    #4 Quando si elimina una squadra non bisogna eliminare i giocatori
    def test_delete_team(self):
        team = Team.objects.get(name="Team A")
        team.delete()
        self.assertEqual(team.is_deleted, True)
        self.assertEqual(Player.objects.filter(team=team).count(), 0)

        self.assertEqual(Team.objects.count(), 2)
        self.assertEqual(Player.objects.count(), 2)

    #4 Quando si elimina una squadra non bisogna eliminare il torneo o i tornei associati
    def test_delete_team_associated_tournaments(self):
        team = Team.objects.get(name="Team A")
        team.delete()
        self.assertEqual(team.is_deleted, True)
        self.assertEqual(team.tournament_set.count(), 1)

        self.assertEqual(Team.objects.count(), 2)
        self.assertEqual(Player.objects.count(), 2)

    #4 Quando si elimina una squadra non bisogna eliminare le partite disputate
    def test_delete_team_associated_matches(self):
        team = Team.objects.get(name="Team A")
        team.delete()
        self.assertEqual(team.is_deleted, True)
        self.assertEqual(team.home_team_match.count(), 1)
        self.assertEqual(team.away_team_match.count(), 1)

    #4 Quando si elimina una squadra non bisogna eliminare le classifiche
    def test_delete_team_associated_placements(self):
        team = Team.objects.get(name="Team A")
        team.delete()
        self.assertEqual(team.is_deleted, True)
        self.assertEqual(team.placement_set.count(), 1)
        self.assertEqual(Placement.objects.count(), 2)

    #4 Quando elimino un torneo le squadre non devono essere cancellate
    def test_delete_tournament(self):
        tournament = Tournament.objects.get(name="Torneo di calcio")
        tournament.delete()
        self.assertEqual(Tournament.objects.count(), 0)
        self.assertEqual(Team.objects.count(), 2)
        self.assertEqual(Player.objects.count(), 2)

    #4 Quando si elimina un utente deve essere cancellato anche i'entità partecipante
    def test_delete_user(self):
        user = User.objects.get(username="antonioverdi")
        user.delete()
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(Player.objects.count(), 1)

    #4 Quando elimino l'entità player non deve essere cancellato l'utente
    def test_delete_player(self):
        player = Player.objects.get(first_name="Antonio")
        player.delete()
        self.assertEqual(Player.objects.count(), 1)
        self.assertEqual(User.objects.count(), 3)
