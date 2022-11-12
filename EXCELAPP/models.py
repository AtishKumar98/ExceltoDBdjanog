from django.db import models

# Create your models here.
class IPL(models.Model):
    city = models.CharField(max_length=250)
    date = models.DateTimeField(default='')
    player_of_match = models.CharField(max_length=250)
    venue = models.CharField(max_length=250)
    neutral_venue = models.CharField(max_length=250)
    team1 = models.CharField(max_length=250)
    team2 = models.CharField(max_length=250)
    toss_winner = models.CharField(max_length=250)
    toss_decision = models.CharField(max_length=250)
    winner = models.CharField(max_length=250)
    result = models.CharField(max_length=250)
    result_margin = models.CharField(max_length=250)
    eliminator = models.CharField(max_length=250)
    method = models.CharField(max_length=250)
    umpire1 = models.CharField(max_length=250)
    umpire2= models.CharField(max_length=250)