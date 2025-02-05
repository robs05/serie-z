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

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['teams'].queryset = Team.objects.filter(owner=user, is_deleted=False)
