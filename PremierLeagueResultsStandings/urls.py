from django.urls import path
from. import views
from. views import register, user_login, login_view


urlpatterns = [
    path('standings/', views.seasons_teams, name='seasons_teams'),
    path('stats/', views.statistics_list, name='statistics_list'),
    path('teaminseson/<int:team_id>', views.team_details, name='team_details'),
    path('add_team_in_season/', views.add_team_in_season, name='add_team_in_season'),
    path('home/', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('add_statistics/<int:team_id>', views.add_statistics, name='add_statistics'),
    path('add_notes/<int:team_id>', views.add_notes, name='add_notes'),
]
