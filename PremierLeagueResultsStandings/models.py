from django.db import models
from django import forms

# Create your models here.
class Team(models.Model):
    # team_seazon_id = models.AutoField(primary_key=True)
    season_End_Year = models.IntegerField()
    team = models.CharField(max_length=100)
    stats = models.ForeignKey('Stats', on_delete=models.SET_NULL, null=True, blank=True)
    notes = models.ForeignKey('Notes', on_delete=models.SET_NULL, null=True, blank=True)

class Stats(models.Model):
    rk = models.IntegerField(null=True)
    mp = models.IntegerField(null=True)
    w = models.IntegerField(null=True)
    d = models.IntegerField(null=True)
    l = models.IntegerField(null=True)
    gf = models.IntegerField(null=True)
    ga = models.IntegerField(null=True)
    gd = models.IntegerField(null=True)
    pts = models.IntegerField(null=True)


class Notes(models.Model):
    notes = models.CharField(max_length=500, null=True)

