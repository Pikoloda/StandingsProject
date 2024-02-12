from django.urls import path
from . import views

urlpatterns = [
    path('standings/', views.seasons_teams, name='seasons_teams'),
    path('stats/', views.statistics_list, name='statistics_list'),
    path('team_details/<int:team_id>', views.team_details, name='team_details'),
    path('add_team_in_season/', views.add_team_in_season, name='add_team_in_season'),
    path('', views.home, name='home'),
    path('add_statistics/<int:team_id>', views.add_statistics, name='add_statistics'),
    path('add_notes/<int:team_id>', views.add_notes, name='add_notes'),
]
