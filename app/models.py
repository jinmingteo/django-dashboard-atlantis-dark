# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Participant(models.Model):
    name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100, unique=True)
    tele_id = models.CharField(max_length=100, unique=True)
    unit = models.CharField(max_length=100)
    pes = models.CharField(max_length=50)
    status = models.CharField(max_length=10)


class Workout(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    date = models.DateTimeField()
    duration = models.DurationField()
    activity = models.CharField(max_length=100)
    calories = models.PositiveSmallIntegerField()
