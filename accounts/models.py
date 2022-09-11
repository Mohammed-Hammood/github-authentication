from random import randint
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.utils import timezone

max_value = 1000000
min_value = 0


class RandomNumberModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    random_number = models.IntegerField(default=randint(min_value, max_value))
    updated_at = models.TimeField(auto_now=True, verbose_name='Updated at (time)')
    timestamp = models.DateField(auto_now_add=True, verbose_name='Created at (date)')

    def last_updated_in_seconds(self):
        time_now = timezone.datetime.now().time()
        seconds = (datetime.combine(date.min, time_now) -  datetime.combine(date.min, self.updated_at)).seconds
        return seconds

    # checks if random number updated last time more than 300 seconds (5 minutes), then it will update random number
    def update_random_number(self):
        if self.last_updated_in_seconds() >= 300:
            self.random_number = randint(min_value, max_value)
            self.save()

    def __str__(self):
        return str(self.random_number)