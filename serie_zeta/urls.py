""" Defines URL patterns for serie_zeta """

from django.urls import path

from . import views

app_name = 'serie_zeta'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('tournaments/', views.tournaments, name='tournaments'),

    # Detail page for a single tournament
    path('tournaments/<int:tournament_id>/', views.tournament, name='tournament'),
]