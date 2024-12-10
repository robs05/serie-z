from django.shortcuts import render

from serie_zeta.models import Tournament, TournamentParticipation


def index(request):
    """The home page for serie_zeta."""
    return render(request, 'serie_zeta/index.html')

def tournaments(request):
    """Show all tournaments."""
    tournaments = Tournament.objects.order_by('start_date')
    context = {'tournaments' : tournaments}
    return render(request, 'serie_zeta/tournaments.html', context)

def tournament(request, tournament_id):
    """Show a single tournament and all its details."""
    tournament = Tournament.objects.get(id=tournament_id)
    tournament_teams = TournamentParticipation.objects.filter(tournament=tournament).order_by('team__name')
    context = {'tournament' : tournament, 'teams' : tournament_teams}
    return render(request, 'serie_zeta/tournament.html', context)