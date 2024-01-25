from django.db import models


# Create your models here.
class Team(models.Model):
    # team_seazon_id = models.AutoField(primary_key=True)
    season_End_Year = models.IntegerField()
    team = models.CharField(max_length=100)
    stats = models.OneToOneField('Stats', on_delete=models.CASCADE, null=True, blank=True)
    notes = models.OneToOneField('Notes', on_delete=models.CASCADE, null=True, blank=True)

class Stats(models.Model):
    rk = models.IntegerField()
    mp = models.IntegerField()
    w = models.IntegerField()
    d = models.IntegerField()
    l = models.IntegerField()
    gf = models.IntegerField()
    ga = models.IntegerField()
    gd = models.IntegerField()
    pts = models.IntegerField()


class Notes(models.Model):
    notes = models.CharField(max_length=500)