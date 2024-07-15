from django.db import models
from django.utils.timezone import now
from datetime import timedelta
from django.utils.timesince import timesince

class Country(models.Model):
    name = models.CharField(max_length=100)
    flag_url = models.URLField()

    def __str__(self):
        return self.name

    def to_dict(self):
            return {
                'name': self.name,
                'flag_url': self.flag_url,
            }

class UserScore(models.Model):
    username = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username}: {self.score}"

    def to_dict(self):
            time_ago= timesince(self.created_at, now())
            return {
                'username': self.username,
                'score': self.score,
                'created_at': f"{time_ago} ago"
            }