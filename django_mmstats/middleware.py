import atexit
import threading

from django.conf import settings


# mmstats requires a single writer per instance, so we must create a mmstats
# instance per thread
tls = threading.local()


class MmStatsMiddleware(object):
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
        request.stats.response_time.start()

    def process_response(self, request, response):
        if hasattr(request, 'stats'):
            request.stats.response_time.stop()
            request.stats.count_status(response.status_code)
        return response

    def process_exception(self, request, exception):
        if hasattr(request, 'stats'):
            request.stats.response_time.stop()
            if hasattr(exception, 'status_code'):
                request.stats.count_status(exception.status_code)
            else:
                request.stats.reqs_err.inc()
