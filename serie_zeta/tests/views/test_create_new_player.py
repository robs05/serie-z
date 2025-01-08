from django.urls import reverse
from django.test import TestCase
from serie_zeta.models import Player
from django.contrib.auth.models import User

class CreateNewPlayerTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='user1', password='P@ssw0rd')
        self.client.login(username='user1', password='P@ssw0rd')
    def test_create_new_player(self):
        response = self.client.get(reverse('serie_zeta:new_player'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'serie_zeta/new_player.html')
        response = self.client.post(reverse('serie_zeta:new_player'),
                                    {'first_name': 'Ciro', 'last_name': 'Mertens', 'birth_date': '1980-01-01',
                                        'position': 'FW', 'captain': False, 'jersey_number': 18}, follow=True)

        if response.context and 'form' in response.context:
            form = response.context['form']
            if not form.is_valid():
                print(form.errors)

        self.assertEqual(response.status_code, 200)

        players = Player.objects.all()
        self.assertEqual(players.count(), 1)
        player = players[0]
        self.assertEqual(player.first_name, 'Ciro')