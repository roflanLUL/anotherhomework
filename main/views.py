import datetime

from django.shortcuts import render, redirect

from main.models import ClickerHistory


def index(request):
    return redirect('/clicker/')


def clicker(request):
    context = {}
    data = ClickerHistory.objects.all()
    santa_counter = 0
    elves_counter = 0
    russian_mail_counter = 0
    item = ClickerHistory(santa=santa_counter, elves=elves_counter, russian_mail=russian_mail_counter,
                          date=datetime.datetime.now())
    # item.save()
    return render(request, 'clicker.html', context)
