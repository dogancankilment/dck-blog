from __future__ import absolute_import
from celery import Celery
from celery import shared_task


@shared_task
def print_hello():
    print 'hello there'


@shared_task
def gen_prime(x):
    multiples = []
    results = []
    for i in xrange(2, x+1):
        if i not in multiples:
            results.append(i)
            for j in xrange(i*i, x+1, i):
                multiples.append(j)
    return results