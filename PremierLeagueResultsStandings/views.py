from django.shortcuts import render, redirect, get_object_or_404
from .models import Team, Stats, Notes
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import AddTeamForm
from django.urls import reverse

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

def team_details(request, id):
    team = get_object_or_404(Team, pk=id)
    stats = team.stats
    notes = team.notes
    return render(request, 'team_details.html', {
        'team': team,
        'stats': stats,
        'notes': notes})

# def add_team_in_season(request):
#     if request.method == 'POST':
#         season = request.POST.get('season')
#         team_name = request.POST.get('team_name')
#
#         # Sprawdź, czy wpisany sezon jest równy lub większy niż ostatni sezon
#         last_season = Team.objects.order_by('-season_End_Year').first()
#         if last_season and int(season) < last_season.season_End_Year:
#             return HttpResponse('Wprowadź poprawny sezon (równy lub większy niż ostatni sezon).')
#
#         # Sprawdź, czy klub już istnieje w danym sezonie
#         if Team.objects.filter(season_End_Year=season, team=team_name).exists():
#             return HttpResponse('Klub jest już uwzględniony w tym sezonie.')
#
#         # Dodaj zespół do bazy danych
#         new_team = Team(season_End_Year=season, team=team_name)
#         new_team.save()
#
#         return HttpResponse(f'Dodano klub "{team_name}" w sezonie {season}.')
#
#     return render(request, 'add_team_in_season.html')


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
    return render(request, 'login.html', {'form': form})

def standings(request):
    # Widok dla strony /standings
    return render(request, 'seasons_teams.html')  # Przykład, proszę dostosować

def user_logout(request):
    logout(request)
    return redirect('home')

def add_team_in_season(request):
    if request.method == 'POST':
        form = AddTeamForm(request.POST)
        if form.is_valid():
            season = form.cleaned_data['season']
            team_name = form.cleaned_data['team_name']

            # Sprawdź, czy wprowadzony sezon jest większy lub równy niż ostatni sezon
            last_season = Team.objects.order_by('-season_End_Year').first()
            if last_season and season < last_season.season_End_Year:
                error_message = "Wprowadź poprawny sezon (równy lub większy niż ostatni sezon)."
                return render(request, 'add_team_in_season.html', {'form': form, 'error_message': error_message})

            # Zapisz nowy zespół w sezonie
            new_team = Team(season_End_Year=season, team=team_name)
            new_team.save()

            return redirect('seasons_teams')
    else:
        form = AddTeamForm()

    return render(request, 'add_team_in_season.html', {'form': form})

from django.contrib.auth.views import LoginView
from django.shortcuts import redirect

class CustomLoginView(LoginView):
    def form_valid(self, form):
        response = super().form_valid(form)
        return response

    def get_success_url(self):
        return reverse('seasons_teams')

login_view = CustomLoginView.as_view()