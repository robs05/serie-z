from django.contrib import admin

from .models import Team, Tournament, Player, Referee, Match, Placement

admin.site.register(Team)
admin.site.register(Tournament)
admin.site.register(Player)
admin.site.register(Referee)
admin.site.register(Match)
admin.site.register(Placement)

