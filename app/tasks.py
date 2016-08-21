from __future__ import absolute_import

from celery import shared_task
from datetime import datetime


@shared_task
def test1(param):
    # run from console: $ celery --app=bigop.celery:celery_app worker --loglevel=info
    t1 = datetime.now()

    # workload
    arr1 = [x for x in xrange(59999999)]
    arr2 = [x for x in xrange(59999999)]
    b = arr1 + arr2

    t2 = datetime.now()
    dif = t2 - t1
    return 'The test task executed in "%s" seconds' % dif