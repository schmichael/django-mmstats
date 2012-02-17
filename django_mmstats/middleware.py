import atexit
import threading

from django.conf import settings


# mmstats (as of 0.4) requires only a single writer per instance, so we need to
# create a mmstats instance per thread
tls = threading.local()


class MmstatsMiddleware(object):
    def __init__(self):
        if not getattr(settings, 'MMSTATS_CLASS', None):
            raise Exception('y u no define settings.MMSTATS_CLASS')
        if not getattr(settings, 'MMSTATS_OPTIONS', None):
            settings.MMSTATS_OPTIONS = {}

    def process_request(self, request):
        if not hasattr(tls, '_mmstats'):
            tls._mmstats = settings.MMSTATS_CLASS(**settings.MMSTATS_OPTIONS)
            atexit.register(tls._mmstats.remove)
        request.stats = tls._mmstats
