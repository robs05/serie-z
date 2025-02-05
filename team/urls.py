""" Defines URL patterns for team """

from django.urls import path

from . import views

app_name = 'team'

urlpatterns = [
    # List of all teams
    path('teams/', views.teams, name='teams'),

    # Detail page for a single team
    path('teams/<int:team_id>/', views.team, name='team'),

    # Page for adding a new team
    path('new_team/', views.new_team, name='new_team'),

    # Page for editing a team
    path('edit_team/<int:team_id>/', views.edit_team, name='edit_team'),

    path('delete_team/<int:team_id>/', views.delete_team, name='delete_team'),
]