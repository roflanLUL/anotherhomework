import datetime

from django.utils import timezone

from django.shortcuts import render, redirect

from main.forms import ClickerForm
from main.models import ClickerHistory


def index(request):
    return redirect('/clicker/')


def clicker(request):
    context = {'pagename': 'New Year Clicker'}
    data = ClickerHistory.objects.all().last()
    if data is None:
        santa_score = 0
        elves_score = 0
        mail_score = 0
    else:
        santa_score = data.santa_score
        elves_score = data.elves_score
        mail_score = data.mail_score
    context['santa_score'] = santa_score
    context['elves_score'] = elves_score
    context['mail_score'] = mail_score

    if request.method == 'POST':
        form = ClickerForm(request.POST)
        if form.is_valid():
            santa_score = int(form.data['santa_score'])
            elves_score = int(form.data['elves_score'])
            mail_score = int(form.data['mail_score'])
            item = ClickerHistory(santa_score=santa_score, elves_score=elves_score, mail_score=mail_score,
                                  date=datetime.datetime.now(tz=timezone.utc))
            item.save()
            return redirect('/clicker/')
        else:
            context['form'] = form
    else:
        context['form'] = ClickerForm()

    return render(request, 'pages/clicker/clicker.html', context)
