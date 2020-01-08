from django.db import models


class ClickerHistory(models.Model):
    santa_score = models.IntegerField()
    elves_score = models.IntegerField()
    mail_score = models.IntegerField()
    date = models.DateTimeField()
