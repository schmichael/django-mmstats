from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^voting$', 'voting.views.voting'),
    url(r'^results$', 'voting.views.results'),
    url(r'^500$', 'voting.views.err'),
)
