from django.shortcuts import render, redirect, get_object_or_404
from .models import Team, Stats, Notes
from django.http import HttpResponse

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

def team_details(request, id):
    team = get_object_or_404(Team, pk=id)
    stats = team.stats
    notes = team.notes
    return render(request, 'team_details.html', {
        'team': team,
        'stats': stats,
        'notes': notes})

def add_team_in_season(request):
    if request.method == 'POST':
        season = request.POST.get('season')
        team_name = request.POST.get('team_name')

        # Sprawdź, czy wpisany sezon jest równy lub większy niż ostatni sezon
        last_season = Team.objects.order_by('-season_End_Year').first()
        if last_season and int(season) < last_season.season_End_Year:
            return HttpResponse('Wprowadź poprawny sezon (równy lub większy niż ostatni sezon).')

        # Sprawdź, czy klub już istnieje w danym sezonie
        if Team.objects.filter(season_End_Year=season, team=team_name).exists():
            return HttpResponse('Klub jest już uwzględniony w tym sezonie.')

        # Dodaj zespół do bazy danych
        new_team = Team(season_End_Year=season, team=team_name)
        new_team.save()

        return HttpResponse(f'Dodano klub "{team_name}" w sezonie {season}.')

    return render(request, 'add_team_in_season.html')
