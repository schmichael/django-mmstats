from django import forms


class MmVotingForm(forms.Form):
    food = forms.CharField(max_length=255)
