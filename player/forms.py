from django import forms

from serie_zeta.models import Player, Team

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
