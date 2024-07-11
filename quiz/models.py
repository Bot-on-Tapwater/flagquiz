from django.db import models

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

    def __str__(self):
        return f"{self.username}: {self.score}"

    def to_dict(self):
            return {
                'username': self.username,
                'score': self.score,
            }