from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from serie_zeta.models import Tournament, TournamentParticipation
from serie_zeta.models import Team

from .forms import TeamForm, TournamentForm

from serie_zeta.utils import position_order

def index(request):
    """The home page for serie_zeta."""
    return render(request, 'serie_zeta/index.html')

@login_required
def tournaments(request):
    """Show all tournaments."""
    tournaments = Tournament.objects.order_by('start_date')
    context = {'tournaments' : tournaments}
    return render(request, 'serie_zeta/tournaments.html', context)

@login_required
def tournament(request, tournament_id):
    """Show a single tournament and all its details."""
    tournament = Tournament.objects.get(id=tournament_id)
    tournament_teams = TournamentParticipation.objects.filter(tournament=tournament).order_by('team__name')
    context = {'tournament' : tournament, 'teams' : tournament_teams}
    return render(request, 'serie_zeta/tournament.html', context)

@login_required
def new_tournament(request):
    """Add a new tournament."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TournamentForm()
    else:
        # POST data submitted; process data.
        form = TournamentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('serie_zeta:tournaments')

    # Display a blank or invalid form.
    context = {'form' : form}
    return render(request, 'serie_zeta/new_tournament.html', context)

@login_required
def edit_tournament(request, tournament_id):
    """Edit an existing tournament."""
    tournament = Tournament.objects.get(id=tournament_id)
    if request.method != 'POST':
        # Initial request; pre-fill form with the current tournament.
        form = TournamentForm(instance=tournament)
    else:
        # POST data submitted; process data.
        form = TournamentForm(instance=tournament, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('serie_zeta:tournaments')

    context = {'tournament' : tournament, 'form' : form}
    return render(request, 'serie_zeta/edit_tournament.html', context)

@login_required
def teams(request):
    """Show all teams."""
    teams = Team.objects.order_by('name')
    context = {'teams' : teams}
    return render(request, 'serie_zeta/teams.html', context)

@login_required
def team(request, team_id):
    """Show a single team and all its details."""
    team = Team.objects.get(id=team_id)
    players = team.player_set.annotate(position_display=position_order).order_by('-position_display')
    context = {'team' : team, 'players' : players}
    return render(request, 'serie_zeta/team.html', context)

@login_required
def new_team(request):
    """Add a new team."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TeamForm()
    else:
        # POST data submitted; process data.
        form = TeamForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('serie_zeta:teams')

    # Display a blank or invalid form.
    context = {'form' : form}
    return render(request, 'serie_zeta/new_team.html', context)

@login_required
def edit_team(request, team_id):
    """Edit an existing team."""
    team = Team.objects.get(id=team_id)
    if request.method != 'POST':
        # Initial request; pre-fill form with the current team.
        form = TeamForm(instance=team)
    else:
        # POST data submitted; process data.
        form = TeamForm(instance=team, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('serie_zeta:teams')

    context = {'team' : team, 'form' : form}
    return render(request, 'serie_zeta/edit_team.html', context)