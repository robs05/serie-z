from django.test import TestCase

from serie_zeta.models import Referee
from django.contrib.auth.models import User

class RefereeTests(TestCase):
    def setUp(self):
        user = User.objects.create_user(username="user", password="password")
        Referee.objects.create(user=user, first_name="A", last_name="B", birth_date="2000-01-01",
                               exeperience=5)

    def test_referee_str(self):
        referee = Referee.objects.get(first_name="A")
        self.assertEqual(str(referee), "A B 5 years of experience")