from celery import Celery


app = Celery('tasks', backend='amqp', broker='amqp://')


@app.task
def print_hello():
    print 'hello there'