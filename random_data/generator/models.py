from django.db import models


class RandomNumber(models.Model):
    number = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.number} at {self.timestamp}'
