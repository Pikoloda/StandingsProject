from django.shortcuts import render, redirect, get_object_or_404
from .models import Team, Stats, Notes
from .forms import AddTeamForm, StatsForm, NotesForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def seasons_teams(request):
    teams_list = Team.objects.all()

    season = request.GET.get('season')
    if season:
        teams_list = teams_list.filter(season_End_Year=season)

    team_name = request.GET.get('team')
    if team_name:
        teams_list = teams_list.filter(team__icontains=team_name)

    paginator = Paginator(teams_list, 15)
    page = request.GET.get('page', 1)
    try:
        teams = paginator.page(page)
    except PageNotAnInteger:
        teams = paginator.page(1)
    except EmptyPage:
        teams = paginator.page(paginator.num_pages)

    seasons = Team.objects.values_list('season_End_Year', flat=True).distinct()

    return render(request, 'seasons_teams.html', {'teams': teams, 'user': request.user, 'seasons': seasons})


def statistics_list(request):
    stats = Stats.objects.all()
    return render(request, 'statistics_list.html', {
        'stats': stats
    })

def team_details(request, team_id):
    team = get_object_or_404(Team, pk=team_id)
    if team.stats:
        stats = team.stats
    else:
        stats = None

    if team.notes:
        notes = team.notes
    else:
        notes = None
    return render(request, 'team_details.html', {'team': team, 'stats': stats, 'notes': notes})

def home(request):
    return render(request, 'home.html')

def standings(request):
    return render(request, 'seasons_teams.html')

def add_team_in_season(request):
    if request.method == 'POST':
        form = AddTeamForm(request.POST)
        if form.is_valid():
            season = form.cleaned_data['season']
            team_name = form.cleaned_data['team_name']
            if Team.objects.filter(season_End_Year=season, team=team_name).exists():
                error_message = "Taki zespół już istnieje w tym sezonie."
                return render(request, 'add_team_in_season.html', {'form': form, 'error_message': error_message})
            if Team.objects.filter(season_End_Year=season).count() >= 20:
                error_message = "Już jest komplet drużyn w tym sezonie."
                return render(request, 'add_team_in_season.html', {'form': form, 'error_message': error_message})
            last_season = Team.objects.order_by('-season_End_Year').first()
            if last_season and season < last_season.season_End_Year:
                error_message = "Wprowadź poprawny sezon (równy lub większy niż ostatni sezon)."
                return render(request, 'add_team_in_season.html', {'form': form, 'error_message': error_message})

            new_team = Team(season_End_Year=season, team=team_name)
            new_team.save()

            stats = Stats.objects.create()
            notes = Notes.objects.create()

            new_team.stats = stats
            new_team.notes = notes
            new_team.save()

            return redirect('add_statistics', team_id=new_team.id)
    else:
        form = AddTeamForm()
    return render(request, 'add_team_in_season.html', {'form': form})

def add_statistics(request, team_id):
    team = get_object_or_404(Team, pk=team_id)

    if request.method == 'POST':
        form = StatsForm(request.POST)
        if form.is_valid():
            cleaned_data = {key: value if value is not None else '' for key, value in form.cleaned_data.items()}
            stats, created = Stats.objects.get_or_create(team=team, defaults=cleaned_data)
            if not created:
                stats.__dict__.update(cleaned_data)
                stats.save()
            return redirect('add_notes', team_id=team.id)
    else:
        form = StatsForm()
    return render(request, 'add_statistics.html', {
        'form': form,
        'team': team,
    })

def add_notes(request, team_id):
    team = get_object_or_404(Team, pk=team_id)

    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            cleaned_data = {key: value if value is not None else '' for key, value in form.cleaned_data.items()}
            notes, created = Notes.objects.get_or_create(team=team, defaults=cleaned_data)
            if not created:
                notes.__dict__.update(cleaned_data)
                notes.save()
            return redirect('team_details', team_id=team_id)
    else:
        form = NotesForm()
    return render(request, 'add_notes.html', {'form': form, 'team': team})
