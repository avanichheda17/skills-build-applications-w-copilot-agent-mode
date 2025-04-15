from djongo import models

class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.email

class Team(models.Model):
    name = models.CharField(max_length=255)
    members = models.ArrayField(model_container=User)

    def __str__(self):
        return self.name

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=255)
    duration = models.IntegerField()  # in minutes
    date = models.DateField()

    def __str__(self):
        return f"{self.user.email} - {self.activity_type}"

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()

    def __str__(self):
        return f"{self.team.name}: {self.points} points"

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout_type = models.CharField(max_length=255)
    duration = models.IntegerField()  # in minutes
    date = models.DateField()

    def __str__(self):
        return f"{self.user.name} - {self.workout_type} on {self.date}"
