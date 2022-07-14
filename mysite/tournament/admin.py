from django.contrib import admin
from .models import MyUser, Player, Tournament, PlayersInTournament

admin.site.register(MyUser)
admin.site.register(Tournament)
admin.site.register(Player)
admin.site.register(PlayersInTournament)