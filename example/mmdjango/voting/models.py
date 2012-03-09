from django.db import models


class MmFood(models.Model):
    food = models.CharField(max_length=255, unique=True)
    votes = models.IntegerField()
