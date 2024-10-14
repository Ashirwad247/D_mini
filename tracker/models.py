from django.db import models
from datetime import timedelta

class Activity(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time_spent = models.DurationField()  # Track time spent on activity
    score = models.IntegerField(default=0)  # Score based on time spent

    def save(self, *args, **kwargs):
        # Automatically calculate score based on time spent (in hours)
        hours_spent = self.time_spent.total_seconds() // 3600
        self.score = int(hours_spent * 10)  # Example: 10 points per hour
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
