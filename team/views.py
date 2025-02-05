from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from serie_zeta.models import Team

from .forms import TeamForm

from serie_zeta.utils import position_order

@login_required
def teams(request):
    """Show all teams."""
    teams = Team.objects.filter(owner=request.user, is_deleted=False).order_by('name')
    context = {'teams' : teams}
    return render(request, 'team/teams.html', context)

@login_required
def team(request, team_id):
    """Show a single team and all its details."""
    team = Team.objects.get(id=team_id)
    if team.owner != request.user:
        raise Http404
    players = team.player_set.annotate(position_display=position_order).order_by('-position_display')
    context = {'team' : team, 'players' : players}
    return render(request, 'team/team.html', context)

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

            return redirect('team:teams')

    # Display a blank or invalid form.
    context = {'form' : form}
    return render(request, 'team/new_team.html', context)

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
            return redirect('team:teams')

    context = {'team' : team, 'form' : form}
    return render(request, 'team/edit_team.html', context)

@login_required
def delete_team(request, team_id):
    """Delete an existing team."""
    print(team_id)
    team = Team.objects.get(id=team_id)
    print(team)
    if team.owner != request.user:
        raise Http404
    team.delete()
    return redirect('team:teams')


