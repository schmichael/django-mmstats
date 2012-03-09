"""Handy base model class for using mmstats with Django apps"""
import mmstats


class BaseDjangoStats(mmstats.MmStats):
    reqs_ok = mmstats.CounterField(label='requests.ok')
    reqs_400 = mmstats.CounterField(label='requests.400')
    reqs_401 = mmstats.CounterField(label='requests.401')
    reqs_403 = mmstats.CounterField(label='requests.403')
    reqs_404 = mmstats.CounterField(label='requests.404')
    reqs_4xx = mmstats.CounterField(label='requests.4xx')
    reqs_err = mmstats.CounterField(label='requests.err')
    response_time = mmstats.TimerField(label='requests.time')

    def count_status(self, status_code):
        """Record http status stats"""
        if status_code >= 200 and status_code < 300:
            self.reqs_ok.inc()
        elif status_code == 401:
            self.reqs_401.inc()
        elif status_code == 403:
            self.reqs_403.inc()
        elif status_code == 404:
            self.reqs_404.inc()
        elif status_code >= 400 and status_code < 500:
            self.reqs_4xx.inc()
        elif status_code >= 500:
            self.reqs_err.inc()
