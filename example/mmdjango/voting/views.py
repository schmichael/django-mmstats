from django import http
from django.shortcuts import render_to_response

from mmdjango.voting import forms, models


def err(request):
    raise Exception('Oh no!')


def voting(request):
    if request.method == 'POST':
        form = forms.MmVotingForm(request.POST)
        if form.is_valid():
            food_name = form.cleaned_data['food']
            try:
                food = models.MmFood.objects.get(food=food_name)
                food.votes += 1
            except models.MmFood.DoesNotExist:
                food = models.MmFood.objects.create(food=food_name, votes=1)
            request.stats.last_vote = food.food
            request.stats.total_votes.inc()
            food.save()
            return http.HttpResponseRedirect('/results')
    else:
        form = forms.MmVotingForm()

    return render_to_response('voting.html', {'form': form})


def results(request):
    top_votes = models.MmFood.objects.order_by('-votes')
    return render_to_response('results.html', {'top_votes': top_votes})
