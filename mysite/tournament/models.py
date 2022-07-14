from email.policy import default
from re import T
from django.db import models
import datetime
from django.contrib.auth.models import User

class MyUser(models.Model):
    email =models.CharField(max_length=30, unique=True)
    name= models.CharField(max_length=30)
    birth_date= models.DateField()

class Tournament(models.Model):
    name= models.CharField(max_length=60, unique=True)
    begin_date= models.DateTimeField()
    end_date= models.DateTimeField(null=True, blank=True)
    max_number_of_player=models.IntegerField()
    creator=models.ForeignKey(User, on_delete=models.DO_NOTHING)


class Player(models.Model):
    name=models.CharField(max_length=50, unique=True)


class PlayersInTournament(models.Model):
    tournament=models.ForeignKey(Tournament, on_delete=models.DO_NOTHING)
    player=models.ForeignKey(Player, on_delete=models.DO_NOTHING)
    class Meta:
        unique_together = ('tournament', 'player',)
