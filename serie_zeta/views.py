from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from serie_zeta.models import Tournament, TournamentParticipation

from .forms import TournamentForm

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


