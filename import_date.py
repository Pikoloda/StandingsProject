import csv
from PremierLeagueResultsStandings.models import Team, Stats, Notes

with open('PremierLeagueStandings.csv', 'r', encoding='utf-8') as input_file:
    data = csv.DictReader(input_file)
    for row in data:
        # Tworzenie zespołu w danym sezonie
        team = Team.objects.create(
            season_End_Year=row['Season_End_Year'],
            team=row['Team']

        )

        # Tworzenie statystyk
        stats = Stats.objects.create(
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

        notes = Notes.objects.create(
            notes=row['Notes']
        )

        team.stats = stats
        team.notes = notes
        team.save()
