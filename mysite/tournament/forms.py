from django import forms
from .models import Tournament, Player
import datetime


class TournamentForm(forms.ModelForm):
    class Meta:
        model=Tournament
        widgets = {
            'begin_date': forms.DateTimeInput(attrs={'type':'datetime-local', 'class':'form-control'},),
            'end_date': forms.DateTimeInput(attrs={'type':'datetime-local', 'class':'form-control'},),
        }
        fields={
            "name",
            "begin_date",
            "max_number_of_player"
        }

class UpdateTournamentForm(forms.ModelForm):
    class Meta:
        model=Tournament
        widgets = {
            'begin_date': forms.DateTimeInput(attrs={'type':'datetime-local', 'class':'form-control'},),
            'end_date': forms.DateTimeInput(attrs={'type':'datetime-local', 'class':'form-control'},),
        }
        exclude=("creator",)

        
    

class PlayerForm(forms.ModelForm):
     class Meta:
        model=Player
        fields={
            "name"
        }