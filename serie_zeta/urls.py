""" Defines URL patterns for serie_zeta """

from django.urls import path

from . import views

app_name = 'serie_zeta'

urlpatterns = [# List of all tournaments
    path('', views.index, name='index'),

    # List of all tournaments
    path('tournaments/', views.tournaments, name='tournaments'),

    # Detail page for a single tournament
    path('tournaments/<int:tournament_id>/', views.tournament, name='tournament'),

    # Page for adding a new tournament
    path('new_tournament/', views.new_tournament, name='new_tournament'),

    # Page for editing a tournament
    path('edit_tournament/<int:tournament_id>/', views.edit_tournament, name='edit_tournament'),

    # List of all teams
    path('teams/', views.teams, name='teams'),

    # Detail page for a single team
    path('teams/<int:team_id>/', views.team, name='team'),

    # Page for adding a new team
    path('new_team/', views.new_team, name='new_team'),

    # Page for editing a team
    path('edit_team/<int:team_id>/', views.edit_team, name='edit_team'),
]