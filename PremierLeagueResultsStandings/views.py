from django.shortcuts import render, redirect, get_object_or_404
from .models import Team, Stats, Notes

# Create your views here.
def season_team(request):
    teams = Team.objects.all()
    return render(request, 'all_season.html', {
        'teams': teams
    })
