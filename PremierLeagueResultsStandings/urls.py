from django.urls import path
from. import views

urlpatterns = [
    path('standings/', views.seasons_teams, name='seasons_teams'),
    path('stats/', views.statistics_list, name='statistics_list'),
    path('teaminseson/<int:id>', views.team_details, name='team_details'),
]
