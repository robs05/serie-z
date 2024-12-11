""" Defines URL patterns for serie_zeta """

from django.urls import path

from . import views

app_name = 'serie_zeta'

urlpatterns = [# List of all tournaments
    path('', views.index, name='index'),


    path('tournaments/', views.tournaments, name='tournaments'),

    # Detail page for a single tournament
    path('tournaments/<int:tournament_id>/', views.tournament, name='tournament'),

    # List of all teams
    path('teams/', views.teams, name='teams'),

    # Detail page for a single team
    path('teams/<int:team_id>/', views.team, name='team'),
]