from django import forms
from .models import Stats, Notes


class AddTeamForm(forms.Form):
    season = forms.IntegerField(label='Sezon', min_value=1, required=False)
    team_name = forms.CharField(label='Nazwa Zespołu', max_length=100, required=False)

    def clean_season(self):
        season = self.cleaned_data.get('season')

        if season and season < 1:
            raise forms.ValidationError("Wprowadź poprawny sezon (równy lub większy niż 1).")

        return season


class StatsForm(forms.ModelForm):
    class Meta:
        model = Stats
        fields = ['rk', 'mp', 'w', 'd', 'l', 'gf', 'ga', 'gd', 'pts']


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['notes']
