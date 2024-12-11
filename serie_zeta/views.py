from django.shortcuts import render

from serie_zeta.models import Tournament, TournamentParticipation
from serie_zeta.models import Team


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

def teams(request):
    """Show all teams."""
    teams = Team.objects.order_by('name')
    context = {'teams' : teams}
    return render(request, 'serie_zeta/teams.html', context)

def team(request, team_id):
    """Show a single team and all its details."""
    team = Team.objects.get(id=team_id)
    players = team.player_set.order_by('position')
    context = {'team' : team, 'players' : players}
    return render(request, 'serie_zeta/team.html', context)