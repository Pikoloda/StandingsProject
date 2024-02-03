from django import forms
from django import forms
from .models import Stats

class AddTeamForm(forms.Form):
    season = forms.IntegerField(label='Sezon', min_value=1)
    team_name = forms.CharField(label='Nazwa Zespołu', max_length=100)

    def clean_season(self):
        """
        Sprawdza, czy sezon jest równy lub większy niż ostatni sezon.
        """
        season = self.cleaned_data.get('season')

        # Tutaj dodaj kod sprawdzający warunek sezonu
        # (np. porównanie z ostatnim sezonem w bazie danych).

        if season < 1:  # Przykładowy warunek
            raise forms.ValidationError("Wprowadź poprawny sezon (równy lub większy niż ostatni sezon).")

        return season

class StatsForm(forms.ModelForm):
    class Meta:
        model = Stats
        fields = ['rk', 'mp', 'w', 'd', 'l', 'gf', 'ga', 'gd', 'pts']
from django import forms
from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['notes']
