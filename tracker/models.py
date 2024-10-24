from django.db import models
from datetime import timedelta, date
import re

class Activity(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time_spent = models.DurationField()  # Track time spent on activity
    score = models.IntegerField(default=0)  # Score based on time spent

    def save(self, *args, **kwargs):
        hours_spent = self.time_spent.total_seconds() / 3600
        base_score = hours_spent * 10  # 10 points per hour

        difficulty_keywords = {
            'easy': 1, 'simple': 1, 'moderate': 2, 'hard': 3, 'challenging': 4
        }
        description = self.description.lower()
        difficulty_score = sum(value for word, value in difficulty_keywords.items() if word in description)
        
        activity_type_score = 0
        if "meeting" in self.name.lower():
            activity_type_score = 5
        elif "exercise" in self.name.lower():
            activity_type_score = 7
        elif "study" in self.name.lower():
            activity_type_score = 8
        
        days_since_activity = (date.today() - self.date).days
        time_decay_factor = max(0, 10 - days_since_activity)  # Score decreases by 1 for each day past 7 days

        self.score = int(base_score + (difficulty_score * 5) + activity_type_score + time_decay_factor)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
