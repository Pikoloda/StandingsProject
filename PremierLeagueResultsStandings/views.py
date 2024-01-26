from django.shortcuts import render, redirect, get_object_or_404
from .models import Team, Stats, Notes

# Create your views here.
def seasons_teams(request):
    teams = Team.objects.all()
    return render(request, 'seasons_teams.html', {
        'teams': teams
    })

def statistics_list(request):
    stats = Stats.objects.all()
    return render(request, 'statistics_list.html', {
        'stats': stats
    })

def team_detail(request, id):
    team = get_object_or_404(Team, pk=id)
    stats = team.stats
    return render(request, 'team_details.html', {'team': team, 'stats': stats})