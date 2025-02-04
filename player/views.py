from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404

from serie_zeta.models import Player

from .forms import PlayerForm
# Create your views here.

@login_required
def players(request):
    """Show all players."""
    players = Player.objects.filter(owner=request.user).order_by('last_name')
    context = {'players' : players}
    return render(request, 'player/players.html', context)



@login_required
def player(request, player_id):
    """Show a single player and all its details."""
    player = Player.objects.get(id=player_id)
    if player.owner != request.user:
        raise Http404
    context = {'player' : player}
    return render(request, 'player/player.html', context)

@login_required
def new_player(request):
    """Add a new player."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = PlayerForm(user=request.user)
    else:
        # POST data submitted; process data.
        form = PlayerForm(data=request.POST)
        if form.is_valid():
            new_player = form.save(commit=False)
            new_player.owner = request.user
            new_player.save()

            return redirect('player:players')

    # Display a blank or invalid form.
    context = {'form' : form}
    return render(request, 'player/new_player.html', context)

@login_required
def edit_player(request, player_id):
    """Edit an existing player."""
    player = Player.objects.get(id=player_id)
    if player.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # Initial request; pre-fill form with the current player.
        form = PlayerForm(instance=player, user=request.user)
    else:
        # POST data submitted; process data.
        form = PlayerForm(instance=player, data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('player:players')

    context = {'player' : player, 'form' : form}
    return render(request, 'player/edit_player.html', context)

@login_required
def delete_player(request, player_id):
    """Delete an existing player."""
    player = Player.objects.get(id=player_id)
    if player.owner != request.user:
        raise Http404
    player.delete()
    return redirect('player:players')