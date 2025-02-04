from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from serie_zeta.models import Tournament, TournamentParticipation
from serie_zeta.models import Team, Player

from .forms import TeamForm, TournamentForm

from serie_zeta.utils import position_order

def index(request):
    """The home page for serie_zeta."""
    return render(request, 'serie_zeta/index.html')

# Tournament ----------------------------
@login_required
def tournaments(request):
    """Show all tournaments."""
    tournaments = Tournament.objects.filter(owner=request.user).order_by('start_date')
    context = {'tournaments' : tournaments}
    return render(request, 'serie_zeta/tournaments.html', context)

@login_required
def tournament(request, tournament_id):
    """Show a single tournament and all its details."""
    tournament = Tournament.objects.get(id=tournament_id)
    # Make sure the tournament belongs to the current user.
    if tournament.owner != request.user:
        raise Http404

    tournament_teams = TournamentParticipation.objects.filter(tournament=tournament, owner=request.user).order_by('team__name')
    context = {'tournament' : tournament, 'teams' : tournament_teams}
    return render(request, 'serie_zeta/tournament.html', context)

@login_required
def new_tournament(request):
    """Add a new tournament."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TournamentForm(user=request.user)
    else:
        # POST data submitted; process data.
        form = TournamentForm(data=request.POST)
        if form.is_valid():
            new_tournament = form.save(commit=False)
            new_tournament.owner = request.user
            new_tournament.save()

            for team in form.cleaned_data['teams']:
                TournamentParticipation.objects.create(tournament=new_tournament, team=team, owner=request.user)

            return redirect('serie_zeta:tournaments')

    # Display a blank or invalid form.
    context = {'form' : form}
    return render(request, 'serie_zeta/new_tournament.html', context)

@login_required
def edit_tournament(request, tournament_id):
    """Edit an existing tournament."""
    tournament = Tournament.objects.get(id=tournament_id)
    if tournament.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # Initial request; pre-fill form with the current tournament.
        form = TournamentForm(instance=tournament, user=request.user)
    else:
        # POST data submitted; process data.
        form = TournamentForm(instance=tournament, data=request.POST, user=request.user)
        if form.is_valid():
            updated_tournament = form.save(commit=False)
            TournamentParticipation.objects.filter(tournament=updated_tournament).delete()
            for team in form.cleaned_data['teams']:
                TournamentParticipation.objects.create(tournament=updated_tournament, team=team, owner=request.user)
            form.save()
            return redirect('serie_zeta:tournaments')

    context = {'tournament': tournament, 'form': form}
    return render(request, 'serie_zeta/edit_tournament.html', context)

@login_required
def delete_tournament(request, tournament_id):
    """Delete an existing tournament."""
    tournament = Tournament.objects.get(id=tournament_id)
    if tournament.owner != request.user:
        raise Http404
    tournament.delete()
    return redirect('serie_zeta:tournaments')

# Team ----------------------------
@login_required
def teams(request):
    """Show all teams."""
    teams = Team.objects.filter(owner=request.user, is_deleted=False).order_by('name')
    context = {'teams' : teams}
    return render(request, 'serie_zeta/teams.html', context)

@login_required
def team(request, team_id):
    """Show a single team and all its details."""
    team = Team.objects.get(id=team_id)
    if team.owner != request.user:
        raise Http404
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
            new_team = form.save(commit=False)
            new_team.owner = request.user
            new_team.save()

            return redirect('serie_zeta:teams')

    # Display a blank or invalid form.
    context = {'form' : form}
    return render(request, 'serie_zeta/new_team.html', context)

@login_required
def edit_team(request, team_id):
    """Edit an existing team."""
    team = Team.objects.get(id=team_id)
    if team.owner != request.user:
        raise Http404
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

@login_required
def delete_team(request, team_id):
    """Delete an existing team."""
    print(team_id)
    team = Team.objects.get(id=team_id)
    print(team)
    if team.owner != request.user:
        raise Http404
    team.delete()
    return redirect('serie_zeta:teams')


