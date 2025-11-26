from djongo import models

class OctofitUser(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'octofit_tracker_user'

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        db_table = 'octofit_tracker_team'

class Activity(models.Model):
    name = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    team = models.CharField(max_length=100)
    class Meta:
        db_table = 'octofit_tracker_activity'

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        db_table = 'octofit_tracker_leaderboard'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        db_table = 'octofit_tracker_workout'
