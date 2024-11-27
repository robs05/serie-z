from django.test import TestCase

from serie_zeta.models import Referee
from django.contrib.auth.models import User

class RefereeTests(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="user", password="password")
        Referee.objects.create(user=user, first_name="A", last_name="B", birth_date="2000-01-01",
                               exeperience=5)

        user1 = User.objects.create_user(username="user1", password="password")
        Referee.objects.create(user=user1, first_name="C", last_name="D", birth_date="2000-01-01",)

    def test_referee_str_with_experience(self):
        referee = Referee.objects.get(first_name="A")
        self.assertEqual(str(referee), "A B 5 years of experience")

    def test_referee_str_without_experience(self):
        referee = Referee.objects.get(first_name="C")
        self.assertEqual(str(referee), "C D")