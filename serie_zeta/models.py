from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=50)
    jersey_color = models.CharField(max_length=50)
    players_num_max = models.IntegerField()

    def __str__(self):
        return self.name

class Tournament(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    teams = models.ManyToManyField(Team)

    def __str__(self):
        return self.name

