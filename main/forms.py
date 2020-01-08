from django import forms


class ClickerForm(forms.Form):
    santa_score = forms.IntegerField()
    elves_score = forms.IntegerField()
    mail_score = forms.IntegerField()
