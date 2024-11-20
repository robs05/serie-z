from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=50)
    jersey_color = models.CharField(max_length=50)
    players_num_max = models.IntegerField()
    is_deleted = models.BooleanField(default=False)

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()

    def __str__(self):
        return self.name

class Tournament(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    teams = models.ManyToManyField(Team, through='TournamentParticipation')

    def __str__(self):
        return self.name

class TournamentParticipation(models.Model):
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, limit_choices_to={'is_deleted': False})
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    participation_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.team.name} in {self.tournament.name} - {self.participation_date}"

class Player(models.Model):
    GOALKEEPER = 'GK'
    DEFENDER = 'DF'
    MIDFIELDER = 'MF'
    FORWARD = 'FW'
    COACH = 'CH'
    POSITION_CHOICES = [
        (GOALKEEPER, 'Portiere'),
        (DEFENDER, 'Difensore'),
        (MIDFIELDER, 'Centrocampista'),
        (FORWARD, 'Attaccante'),
        (COACH, 'Allenatore'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    position = models.CharField(max_length=50, choices=POSITION_CHOICES)
    captain = models.BooleanField()
    jersey_number = models.IntegerField()
    # The player belongs to a team and if code is 0 the player is not part of any team
    team = models.ForeignKey(Team, on_delete=models.SET(0))

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Placement(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    placement_code = models.CharField(max_length=50)
    points = models.IntegerField()
    goal_difference = models.IntegerField()
    goals_scored = models.IntegerField()
    goals_conceded = models.IntegerField()
    matches_played = models.IntegerField()
    matches_won = models.IntegerField()
    matches_drawn = models.IntegerField()
    matches_lost = models.IntegerField()

    def __str__(self):
        return f"{self.team.name} - {self.placement_code} - {self.points} points"

class Match(models.Model):

    # to verify
    home_team = models.ForeignKey(Team, on_delete=models.SET_NULL, related_name='home_team', null=True)
    away_team = models.ForeignKey(Team, on_delete=models.SET_NULL, related_name='away_team', null=True)
    home_team_goals = models.IntegerField()
    away_team_goals = models.IntegerField()
    match_date = models.DateTimeField()

    def __str__(self):
        return f"{self.home_team.name}({self.home_team_goals}) vs {self.away_team.name}({self.away_team_goals})  - {self.match_date}"

class Referee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    exeperience = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.exeperience} years of experience"