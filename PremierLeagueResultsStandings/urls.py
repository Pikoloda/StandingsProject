from django.urls import path
from. import views

urlpatterns = [
    path('standings/', views.season_team, name='season_team'),

]
