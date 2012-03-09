import mmstats
from django_mmstats import base


class DjangoStats(base.BaseDjangoStats):
    last_vote = mmstats.StringField(label='votes.last')
    total_votes = mmstats.CounterField(label='votes.total')
