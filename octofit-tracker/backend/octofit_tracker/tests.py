from django.test import TestCase
from .models import OctofitUser, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = OctofitUser.objects.create(email='test@example.com', username='testuser', team='Marvel')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.team, 'Marvel')

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Marvel')
        self.assertEqual(team.name, 'Marvel')

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(name='Run', user_email='test@example.com', team='Marvel')
        self.assertEqual(activity.name, 'Run')
        self.assertEqual(activity.user_email, 'test@example.com')
        self.assertEqual(activity.team, 'Marvel')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(team='Marvel', points=100)
        self.assertEqual(leaderboard.team, 'Marvel')
        self.assertEqual(leaderboard.points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Pushups', description='Do 50 pushups')
        self.assertEqual(workout.name, 'Pushups')
        self.assertEqual(workout.description, 'Do 50 pushups')
