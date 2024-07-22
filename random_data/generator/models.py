from django.db import models


# Model to store random numbers
class RandomNumber(models.Model):
    # Field to store the random number
    number = models.IntegerField()
    # Timestamp of when the record was created
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.number} at {self.timestamp}'