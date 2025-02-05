"""Defines URL patterns for player."""

from django.urls import path

from . import views

app_name = 'player'

urlpatterns = [
    # List of all players
    path('players/', views.players, name='players'),

    # Detail page for a single player
    path('players/<int:player_id>/', views.player, name='player'),

    # Page for adding a new player
    path('new_player/', views.new_player, name='new_player'),

    # Page for editing a player
    path('edit_player/<int:player_id>/', views.edit_player, name='edit_player'),

    # Delete a player
    path('delete_player/<int:player_id>/', views.delete_player, name='delete_player')
]