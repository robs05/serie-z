from django import forms

from serie_zeta.models import Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'jersey_color', 'players_num_max']
        labels = {
            'name': 'Nome',
            'jersey_color': 'Colore maglia',
            'players_num_max': 'Num. max giocatori'
        }
