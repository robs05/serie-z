from django.shortcuts import render

from serie_zeta.models import Tournament


def index(request):
    """The home page for serie_zeta."""
    return render(request, 'serie_zeta/index.html')

def tournaments(request):
    """Show all tournaments."""
    tournaments = Tournament.objects.order_by('start_date')
    context = {'tournaments' : tournaments}
    return render(request, 'serie_zeta/tournaments.html', context)