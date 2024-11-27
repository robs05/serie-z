from django.test import TestCase

from serie_zeta.models import Tournament

class TournamentTests(TestCase):
    def setUp(self):
        Tournament.objects.create(name="Torneo di calcio", code="T2021", description="Torneo di calcio amatoriale",
                                  start_date="2021-06-01", end_date="2021-06-30")

    def test_tournament_name(self):
        tournament = Tournament.objects.get(name="Torneo di calcio")
        self.assertEqual(tournament.name, "Torneo di calcio")

    def test_tournament_code(self):
        tournament = Tournament.objects.get(code="T2021")
        self.assertEqual(tournament.code, "T2021")

    def test_tournament_description(self):
        tournament = Tournament.objects.get(name="Torneo di calcio")
        self.assertEqual(tournament.description, "Torneo di calcio amatoriale")

    def test_tournament_start_date(self):
        tournament = Tournament.objects.get(name="Torneo di calcio")
        self.assertEqual(tournament.start_date.strftime("%Y-%m-%d"), "2021-06-01")

    def test_tournament_end_date(self):
        tournament = Tournament.objects.get(name="Torneo di calcio")
        self.assertEqual(tournament.start_date.strftime("%Y-%m-%d"), "2021-06-01")

    def test_tournament_str(self):
        tournament = Tournament.objects.get(name="Torneo di calcio")
        self.assertEqual(str(tournament), "Torneo di calcio - T2021")
