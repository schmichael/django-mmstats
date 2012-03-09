=====
About
=====

Mmstats is a way to expose and read diagnostic values and metrics for
applications. Think of mmstats as /proc for your application.

This project is an integration between mmstats and Django and includes a base
mmstats model class (see ``django_mmstats/base.py``) and middleware (see
``django_mmstats/middleware.py``).

The middleware will create a ``request.stats`` mmstats instance on all request
objects record basic metrics like average response time and counters for each
status code.


=====
Usage
=====

See ``example/mmdjango`` for a full example of integrating Django and MmStats!

Step 0: pip install django-mmstats
----------------------------------

Install django-mmstats in your Django project's Python path.


Step 1: Create your own stats class
-----------------------------------

Create your own stats subclass. It can be as simple as:

::

   from django_mmstats.base import BaseDjangoStats

   class DjangoStats(BaseDjangoStats):
       """Add mmstats fields here, just like Django models!"""


Step 2: Edit your settings.py
-----------------------------

Make sure you include ``django_mmstats.middleware.MmStatsMiddleware`` in your
``MIDDLEWARE_CLASSES``.

Then add the following settings so the middleware knows where to find your stats:

::

    # MmStats Settings!
    import stats
    MMSTATS_CLASS = stats.DjangoStats  # Required
    MMSTATS_OPTIONS = {}               # Optional kwargs to pass to MMSTATS_CLASS


Step 3: Test it out!
--------------------

Run Django's test server and hit a couple pages. Then run ``slurpstats
$TMP/mmstats-*`` to see the stats collected!
