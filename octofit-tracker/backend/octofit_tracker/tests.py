from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(email="test@example.com", name="Test User", password="password123")
        self.assertEqual(user.email, "test@example.com")

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="Team A")
        self.assertEqual(team.name, "Team A")

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create(email="test@example.com", name="Test User", password="password123")
        activity = Activity.objects.create(user=user, activity_type="Running", duration=30, date="2025-04-15")
        self.assertEqual(activity.activity_type, "Running")

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name="Team A")
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(leaderboard.points, 100)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        user = User.objects.create(email="test@example.com", name="Test User", password="password123")
        workout = Workout.objects.create(user=user, workout_type="Yoga", duration=60, date="2025-04-15")
        self.assertEqual(workout.workout_type, "Yoga")
