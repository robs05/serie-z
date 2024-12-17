from django import forms

from .models import Team, Tournament

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['name', 'code', 'description', 'start_date', 'end_date', 'teams']
        labels = {
            'name': 'Nome',
            'code': 'Codice',
            'description': 'Descrizione',
            'start_date': 'Data inizio',
            'end_date': 'Data fine',
            'teams': 'Squadre',
        }
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'teams': forms.SelectMultiple(attrs={'required': False}),
        }


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'jersey_color', 'players_num_max']
        labels = {
            'name': 'Nome',
            'jersey_color': 'Colore maglia',
            'players_num_max': 'Num. max giocatori'
        }