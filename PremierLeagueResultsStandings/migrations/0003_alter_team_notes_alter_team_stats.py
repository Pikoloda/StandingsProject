# Generated by Django 5.0.1 on 2024-02-04 13:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PremierLeagueResultsStandings', '0002_load_initial_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='notes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='PremierLeagueResultsStandings.notes'),
        ),
        migrations.AlterField(
            model_name='team',
            name='stats',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='PremierLeagueResultsStandings.stats'),
        ),
    ]
