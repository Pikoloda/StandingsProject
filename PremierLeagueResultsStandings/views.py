from django.shortcuts import render, redirect, get_object_or_404
from .models import Team, Stats, Notes
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.views import LoginView
from .forms import AddTeamForm
from .forms import StatsForm
from .forms import NotesForm

def seasons_teams(request):
    teams = Team.objects.all()
    return render(request, 'seasons_teams.html', {
        'teams': teams,
        'user': request.user
    })


def statistics_list(request):
    stats = Stats.objects.all()
    return render(request, 'statistics_list.html', {
        'stats': stats
    })


# def team_details(request, id):
#     team = get_object_or_404(Team, pk=id)
#     stats = team.stats
#     notes = team.notes
#     return render(request, 'team_details.html', {
#         'team': team,
#         'stats': stats,
#         'notes': notes})

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


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Przekierowanie do season_teams.html po udanej rejestracji
            return redirect('seasons_teams')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Przekieruj do /standings lub innej strony
            return render(request, 'seasons_teams.html')  # Przykład, proszę dostosować
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def standings(request):
    # Widok dla strony /standings
    return render(request, 'seasons_teams.html')  # Przykład, proszę dostosować


def user_logout(request):
    logout(request)
    return redirect('home')


class CustomLoginView(LoginView):
    def form_valid(self, form):
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse('seasons_teams')


login_view = CustomLoginView.as_view()


# def add_team_in_season(request):
#     if request.method == 'POST':
#         form = AddTeamForm(request.POST)
#         if form.is_valid():
#             season = form.cleaned_data['season']
#             team_name = form.cleaned_data['team_name']
#
#             # Sprawdź, czy zespół o danej nazwie już istnieje w danym sezonie
#             if Team.objects.filter(season_End_Year=season, team=team_name).exists():
#                 error_message = "Taki zespół już istnieje w tym sezonie."
#                 return render(request, 'add_team_in_season.html', {'form': form, 'error_message': error_message})
#
#             # Sprawdź, czy sezon nie ma już 20 drużyn
#             if Team.objects.filter(season_End_Year=season).count() >= 20:
#                 error_message = "Już jest komplet drużyn w tym sezonie."
#                 return render(request, 'add_team_in_season.html', {'form': form, 'error_message': error_message})
#
#             # Sprawdź, czy wprowadzony sezon jest większy lub równy niż ostatni sezon
#             last_season = Team.objects.order_by('-season_End_Year').first()
#             if last_season and season < last_season.season_End_Year:
#                 error_message = "Wprowadź poprawny sezon (równy lub większy niż ostatni sezon)."
#                 return render(request, 'add_team_in_season.html', {'form': form, 'error_message': error_message})
#
#             # Zapisz nowy zespół w sezonie
#             new_team = Team(season_End_Year=season, team=team_name)
#             new_team.save()
#
#             return redirect('seasons_teams')
#         else:
#             error_message = "Wprowadź poprawne dane."
#     else:
#         form = AddTeamForm()
#         error_message = None
#
#     return render(request, 'add_team_in_season.html', {'form': form, 'error_message': error_message})


# def add_team_in_season(request):
#     if request.method == 'POST':
#         form = AddTeamForm(request.POST)
#         if form.is_valid():
#             season = form.cleaned_data['season']
#             team_name = form.cleaned_data['team_name']
#
#             # Sprawdź, czy zespół o danej nazwie już istnieje w danym sezonie
#             if Team.objects.filter(season_End_Year=season, team=team_name).exists():
#                 error_message = "Taki zespół już istnieje w tym sezonie."
#                 return render(request, 'add_team_in_season.html', {'form': form, 'error_message': error_message})
#
#             # Sprawdź, czy sezon nie ma już 20 drużyn
#             if Team.objects.filter(season_End_Year=season).count() >= 20:
#                 error_message = "Już jest komplet drużyn w tym sezonie."
#                 return render(request, 'add_team_in_season.html', {'form': form, 'error_message': error_message})
#
#             # Sprawdź, czy wprowadzony sezon jest większy lub równy niż ostatni sezon
#             last_season = Team.objects.order_by('-season_End_Year').first()
#             if last_season and season < last_season.season_End_Year:
#                 error_message = "Wprowadź poprawny sezon (równy lub większy niż ostatni sezon)."
#                 return render(request, 'add_team_in_season.html', {'form': form, 'error_message': error_message})
#
#             # Zapisz nowy zespół w sezonie
#             new_team = Team(season_End_Year=season, team=team_name)
#             new_team.save()
#
#             # Przekieruj na stronę z dodatkowymi informacjami o drużynie
#             return redirect('team_details', id=new_team.id)
#
#     else:
#         form = AddTeamForm()
#
#     return render(request, 'add_team_in_season.html', {'form': form})
#     return redirect('add_statistics', team_id=newly_created_team.id)
#
#     return render(request, 'add_team_in_season.html')

def add_team_in_season(request):
    if request.method == 'POST':
        form = AddTeamForm(request.POST)
        if form.is_valid():
            season = form.cleaned_data['season']
            team_name = form.cleaned_data['team_name']

            # Sprawdź, czy zespół o danej nazwie już istnieje w danym sezonie
            if Team.objects.filter(season_End_Year=season, team=team_name).exists():
                error_message = "Taki zespół już istnieje w tym sezonie."
                return render(request, 'add_team_in_season.html', {'form': form, 'error_message': error_message})

            # Sprawdź, czy sezon nie ma już 20 drużyn
            if Team.objects.filter(season_End_Year=season).count() >= 20:
                error_message = "Już jest komplet drużyn w tym sezonie."
                return render(request, 'add_team_in_season.html', {'form': form, 'error_message': error_message})

            # Sprawdź, czy wprowadzony sezon jest większy lub równy niż ostatni sezon
            last_season = Team.objects.order_by('-season_End_Year').first()
            if last_season and season < last_season.season_End_Year:
                error_message = "Wprowadź poprawny sezon (równy lub większy niż ostatni sezon)."
                return render(request, 'add_team_in_season.html', {'form': form, 'error_message': error_message})

            # Zapisz nowy zespół w sezonie
            new_team = Team(season_End_Year=season, team=team_name)
            new_team.save()

            # Przekieruj na stronę z dodatkowymi informacjami o drużynie
            return redirect('add_statistics', team_id=new_team.id)

    else:
        form = AddTeamForm()

    return render(request, 'add_team_in_season.html', {'form': form})


def add_statistics(request, team_id):
    team = get_object_or_404(Team, pk=team_id)

    if request.method == 'POST':
        form = StatsForm(request.POST)
        if form.is_valid():
            stats = form.save(commit=False)
            stats.team = team
            stats.save()

            # Przekieruj na stronę zespołu
            return redirect('seasons_teams')

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
            notes = form.save(commit=False)
            notes.team = team
            notes.save()
            return redirect('team_details', team_id=team_id)
    else:
        form = NotesForm()

    return render(request, 'add_notes.html', {'form': form, 'team': team})
