from django.db import models


class ClickerHistory(models.Model):
    santa = models.IntegerField()
    elves = models.IntegerField()
    russian_mail = models.IntegerField()
    date = models.DateTimeField()
