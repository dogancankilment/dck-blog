from celery import Celery

app = Celery('tasks', backend='amqp', broker='amqp://')


@app.task
def print_hello():
    print 'hello there'


@app.task
def gen_prime(x):
    multiples = []
    results = []
    for i in xrange(2, x+1):
        if i not in multiples:
            results.append(i)
            for j in xrange(i*i, x+1, i):
                multiples.append(j)
    return results

if __name__ == '__main__':
    primes = gen_prime.delay(5000)
    print primes.get()
    print primes.ready()
