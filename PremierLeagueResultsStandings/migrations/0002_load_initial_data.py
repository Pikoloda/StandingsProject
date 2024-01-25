import csv

from django.db import migrations

from ..models import Team, Stats, Notes


def load_initial_data(apps, schema_editor):
    with open('PremierLeagueStandings.csv', 'r', encoding='utf-8') as input_file:
        data = csv.DictReader(input_file, delimiter=',')
        for row in data:
            # Tworzenie nowego zestawu Stats dla każdego wiersza
            team_stats = Stats.objects.create(
                rk=row['Rk'],
                mp=row['MP'],
                w=row['W'],
                d=row['D'],
                l=row['L'],
                gf=row['GF'],
                ga=row['GA'],
                gd=row['GD'],
                pts=row['Pts']
            )

            # Tworzenie nowego zestawu Notes dla każdego wiersza
            team_notes = Notes.objects.create(
                notes=row['Notes']
            )

            # Tworzenie nowego obiektu Team i przypisanie do niego utworzonych zestawów Stats i Notes
            Team.objects.create(
                season_End_Year=row['Season_End_Year'],
                team=row['Team'],
                stats=team_stats,
                notes=team_notes
            )


class Migration(migrations.Migration):
    dependencies = [
        ('PremierLeagueResultsStandings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_initial_data),
    ]
