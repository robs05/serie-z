from django import forms

from .models import Team, Tournament, Player

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

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['teams'].queryset = Team.objects.filter(owner=user, is_deleted=False)

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'jersey_color', 'players_num_max']
        labels = {
            'name': 'Nome',
            'jersey_color': 'Colore maglia',
            'players_num_max': 'Num. max giocatori'
        }


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ['first_name', 'last_name', 'birth_date', 'position', 'captain', 'jersey_number', 'team']
        labels = {
            'first_name': 'Nome',
            'last_name': 'Cognome',
            'birth_date': 'Data di nascita',
            'position': 'Ruolo',
            'captain': 'Capitano',
            'jersey_number': 'Numero maglia',
            'team': 'Squadra',
        }
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'team': forms.Select(attrs={'required': False}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['team'].queryset = Team.objects.filter(owner=user, is_deleted=False)